from urllib.request import urlopen
from selenium import webdriver
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import requests
from lxml import html
from selenium import webdriver

# import urllib2
from bs4 import BeautifulSoup
import smtplib
import os.path as op
import sched
import time
import schedule
import xlsxwriter
import os

class RadioScrapping:

    # class attributes
    scrapping_link = ""
    browser = object

    def __init__(self, scrapping_link):
        self.scrapping_link = "https://www.radia.sk/radia/fun/playlist"
        self.browser = webdriver.PjantomJS()
        self.browser.get(scrapping_link)

    
    def relocate(self, months):
        self.browser.execute_script("$('#playlist_filter_date').click()")
        for i in months:
            self.browser.execute_script('''$('div[data-action="prev"]').click()''')

        self.browser.execute_script("$('.day').click()")
        self.browser.execute_script("$('.blue').click()")
    
    def chcekAndSend(self):

        try:
            y = 0
            x = 0
            z = 0
            datum = 0
            upto25 = 0
            datum_space = "06"
            cellLocation = "A"
            klikanie = 0

            for xx in range(10):
                print(xx)
                page = browser.page_source
                soup = BeautifulSoup(page, "html.parser")

                # only up to 25

                for data in soup.find_all("span", {"class": "datum"}):

                    text = data.decode()
                    text = text[text.find(">") + 1 : text.find("/") - 1]

                    if (
                        datum_space
                        != text[text.find(".") + 1 : text.find(".") + 3]
                    ):
                        datum_space = text[
                            text.find(".") + 1 : text.find(".") + 3
                        ]
                        cellLocation = chr(ord(cellLocation) + 3)

                    worksheet.write(
                        chr(ord(cellLocation) + 2) + str(datum), text
                    )

                    datum = datum + 1
                for data in soup.find_all("div", {"class": "titul"}):

                    if upto25 == 25:
                        upto25 = 0
                        break
                    upto25 = upto25 + 1
                    text = data.decode()
                    text = text[text.find(">") + 1 : text.find("/") - 1]

                    worksheet.write(cellLocation + str(x), text)
                    x = x + 1

                for data in soup.find_all("div", {"class": "interpret"}):

                    if upto25 == 25:
                        upto25 = 0
                        break
                    upto25 = upto25 + 1
                    text = data.decode()
                    text = text[text.find(">") + 1 : text.find("/") - 1]

                    worksheet.write(chr(ord(cellLocation) + 1) + str(z), text)
                    z = z + 1
                # this is for date

                browser.execute_script("$('.dopredu').click()")

                time.sleep(1)

                y = y + 1
            print("koniec")

        except Exception as e:
            print(e)

    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook("DATABASE.xlsx")
    # workbook = xlsxwriter.Workbook(os.path.join(os.path.dirname(os.path.abspath("C:/Users/Patrik/Desktop/radio")),"result.xlsx"))
    worksheet = workbook.add_worksheet()
    # Widen the first column to make the text clearer.
    worksheet.set_column("A:A", 20)
    worksheet.set_column("B:B", 20)
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({"bold": True})
    worksheet.write("A1", "skupina")
    worksheet.write("A2", "World")
    print("excel created")
    chcekAndSend()
    workbook.close()
