
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sys
import re

class RadioScrapping:

    # class attributes - unique to class
    # note that class attributes are shared betwen instances of the class
    # since we are creating always just one object it is one
    __browser = webdriver.PhantomJS()
    __scrapped_element_position = 0
    __excel_offset = 2

    __date_location = 0
    __title_location = 1
    __author_location = 2

    # initialize PhantomJS and BeautifulSoup
    def __init__(self, scrapping_link, excel_handler):
        # object attributes - unique to instance
        self.__scrapping_link = scrapping_link
        self.__excel_handler = excel_handler
        self.__soup = object
        self.__browser.get(self.__scrapping_link)
    
    # reload and load source
    def __refresh(self):
        # return source of the page
        page = self.__browser.page_source
        # create soup
        self.__soup = BeautifulSoup(page, "html.parser")
        

    # relocate X months back
    # there is a data picker on the top
    def relocate(self, months):
        for i in range(months):
            #print("relocating")
            # only this fails even object is inicialized, since it gets 404 header or something like that
            try:
                self.__browser.execute_script(
                    """$('div[data-action="prev"]').click()"""
                )
                #print('script executed')
            except Exception as e:
                print("Could not execute script\nCheck if url provided is correct")
                print(str(e)[:100] + " ...")
                print("Exiting...")
                sys.exit()

        self.__browser.execute_script("$('.datepicker--cell').click()")
        self.__browser.execute_script("$('#playlist_filter_button').click()")
        # sleep around 10 second till AJAX request is done loding
        time.sleep(10)

        self.__refresh()


    # scrapping -> date of the song
    def __getTheDate(self):
        i = 0
        for data in self.__soup.find_all("span", class_= ["playlist" , "datum"]):

            text = data.decode()
            date = text[text.find(">") + 1 : text.find("/") - 1]
            self.__excel_handler.write(i + self.__scrapped_element_position + self.__excel_offset, self.__date_location, date)
            i += 1  

    # scrapping -> title of the song
    def __getTheTitle(self):
        i = 0
        for data in self.__soup.select('.playlist .titul'):
            text = data.decode()
            title = text[text.find(">") + 1 : text.find("/") - 1]
            self.__excel_handler.write(i + self.__scrapped_element_position + self.__excel_offset, self.__title_location, title)
            i += 1

    # scrapping -> author of the song
    def __getTheAuthor(self):
        i = 0
        for data in self.__soup.select('.playlist .interpret'):
            text = data.decode()
            author = text[text.find(">") + 1 : text.find("/") - 1]
            self.__excel_handler.write(i +self.__scrapped_element_position + self.__excel_offset, self.__author_location, author)
            i += 1

    def scraping(self, number_of_pages):
        print("Scrapping from", self.__scrapping_link)
        for _ in range(number_of_pages):
            self.__refresh()
            time.sleep(3)
            self.__getTheDate()
            self.__getTheAuthor()
            self.__getTheTitle()
            self.__browser.execute_script("$('.dozadu').click()")
            self.__scrapped_element_position += 50
            # some sleep to ensure everything goes well
            time.sleep(3)

        print("finished")
        self.__excel_handler.close()
