
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sys

class RadioScrapping:

    # class attributes - unique to class
    # note that class attributes are shared betwen instances of the class
    # since we are creating always just one object it is one
    __browser = webdriver.PhantomJS()
    __scrapped_element_position = 0
    __excel_offset = 2
    __date_location = 1
    __title_location = 2
    __author_location = 3

    def __init__(self, scrapping_link, excel_handler):
        # object attributes - unique to instance
        self.__scrapping_link = scrapping_link
        self.__excel_handler = excel_handler
        self.__soup = object
        self.__browser.get(self.__scrapping_link)
    

    # initialize PhantomJS and BeautifulSoup
    def __refresh(self):
        # return source of the page
        page = self.__browser.page_source
        # create soup
        self.__soup = BeautifulSoup(page, "html.parser")


    # relocate X months back
    # there is a data picker on the top
    def relocate(self, months):
        for i in range(months):
            print("relocating")
            # only this fails even object is inicialized, since it gets 404 header or something like that
            try:
                self.__browser.execute_script(
                    """$('div[data-action="prev"]').click()"""
                )
                print('script executed')
            except Exception as e:
                print("Could not execute script\nCheck if url provided is correct")
                print(str(e)[:100] + " ...")
                print("Exiting...")
                sys.exit()
            # time.sleep(2)

        # time.sleep(3)
        self.__browser.execute_script("$('.datepicker--cell').click()")
        # sleep around 10 second till AJAX request is done loding

        self.__browser.execute_script("$('#playlist_filter_button').click()")
        time.sleep(10)

        print(self.__browser.current_url)

        self.__refresh()



    # scrapping -> date of the song
    def __getTheDate(self):
        # get the date
        for data in self.__soup.find_all("span", {"class": "datum"}):
            text = data.decode()
            date = text[text.find(">") + 1 : text.find("/") - 1]
            
            print(date)
            self.__excel_handler.write(self.__scrapped_element_position + self.__excel_offset, self.__date_location, date)

            # excel
            #cellLocation = chr(ord(cellLocation) + 3)
            # if datum_space != text[text.find(".") + 1 : text.find(".") + 3]:
            #     datum_space = text[text.find(".") + 1 : text.find(".") + 3]

            # # worksheet.write(chr(ord(cellLocation) + 2) + str(datum), text)
            # datum = datum + 1



    # scrapping -> title of the song
    def __getTheTitle(self):
        for data in self.__soup.find_all("div", {"class": "titul"}):
            text = data.decode()
            title = text[text.find(">") + 1 : text.find("/") - 1]
            print(title)
            self.__excel_handler.write(self.__scrapped_element_position + self.__excel_offset, self.__title_location, title)

            # worksheet.write(cellLocation + str(cellStart), text)
            # cellStart = cellStart + 1



    # scrapping -> author of the song
    def __getTheAuthor(self):
        for data in self.__soup.find_all("div", {"class": "interpret"}):
            text = data.decode()
            author = text[text.find(">") + 1 : text.find("/") - 1]
            print(author)
            self.__excel_handler.write(self.__scrapped_element_position + self.__excel_offset, self.__author_location, author)

            # worksheet.write(chr(ord(cellLocation) + 1) + str(cellEnd), text)
            # cellEnd = cellEnd + 1
        # this is for date



    def scraping(self, number_of_pages):
        print("Scrapping from", self.__scrapping_link)

        cellStart = 0
        cellEnd = 0
        datum = 0
        upto25 = 0
        datum_space = "06"
        cellLocation = "A"

        for i in range(number_of_pages):
            print(number_of_pages)
            self.__getTheDate()
            # self.__getTheAuthor()
            # self.__getTheTitle()
            self.__browser.execute_script("$('.dopredu').click()")
            self.__refresh()

            

            # some sleep to ensure everything goes well
            time.sleep(3)
            self.__scrapped_element_position += 1

        print("koniec")
        self.__excel_handler.close()

