from urllib.request import urlopen
from selenium import webdriver
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import requests
from lxml import html
from selenium import webdriver
#import urllib2
from bs4 import BeautifulSoup
import smtplib
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import sched
import time
import schedule
import xlsxwriter
import os


def chcekAndSend():
    
    link2 = "https://www.radia.sk/radia/fun/playlist"
    try:
        print(link2)
        print("this is a link")
        file = open('testfile.txt', 'r+')
        file.read()

        with open('testfile.txt') as myfile:

            if link2 in myfile.read():
                print('Ou this project has been visited')
                print('\n')

            else:
                file.truncate()
                open("testfile.txt", 'w').close()
                open("testfile.txt", 'r+')
                # file.write(link2)
                print("Writing to the file")
                browser = webdriver.PhantomJS()
                browser.get(link2)
                #$("#playlist_date_filter").click()
                browser.execute_script("$('#playlist_date_filter').click()")
                browser.execute_script("$('.prev').click()")
                browser.execute_script("$('.prev').click()")
                browser.execute_script("$('.prev').click()")
                browser.execute_script("$('.prev').click()")
                
                browser.execute_script("$('.prev').click()")
                browser.execute_script("$('.day').click()")
                browser.execute_script("$('.blue').click()")
                
                
                
                

                
                y = 0
                x = 0
                z = 0
                datum = 0
                upto25 = 0
                datum_space = '06'
                cellLocation = 'A'
                klikanie = 0
                for xx in range(1000):
                    print(xx)
                    page = browser.page_source
                    soup = BeautifulSoup(page, 'html.parser')
                  
                   # only up to 25
                    
                    for data in soup.find_all('span', {'class': 'datum'}):

                        text = data.decode()
                        text = text[text.find('>')+1:text.find('/')-1]
                      
                        if datum_space != text[text.find('.')+1:text.find('.')+3]:
                            datum_space = text[text.find('.')+1:text.find('.')+3]
                            cellLocation = chr(ord(cellLocation) + 3)
                        


                        worksheet.write(chr(ord(cellLocation) + 2)+str(datum), text)
                        
                        datum = datum+1
                    for data in soup.find_all('div', {'class': 'titul'}):
                        
                        if upto25 == 25:
                            upto25 = 0
                            break
                        upto25 = upto25+1    
                        text = data.decode()
                        text = text[text.find('>')+1:text.find('/')-1]
                     

                        worksheet.write(cellLocation+str(x), text)
                        x = x+1
                   
                    for data in soup.find_all('div', {'class': 'interpret'}):
                       
                        if upto25 == 25:
                            upto25 = 0
                            break
                        upto25 = upto25+1    
                        text = data.decode()
                        text = text[text.find('>')+1:text.find('/')-1]
                    
                        worksheet.write(chr(ord(cellLocation) + 1)+str(z), text)
                        z = z+1
                     #this is for date
                   

                    browser.execute_script("$('.dopredu').click()")

                    time.sleep(1)

                    y = y+1
                print("koniec")
        file.close()
       
    except Exception as e:
        print(e)



# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('DATABASE.xlsx')
#workbook = xlsxwriter.Workbook(os.path.join(os.path.dirname(os.path.abspath("C:/Users/Patrik/Desktop/radio")),"result.xlsx"))
worksheet = workbook.add_worksheet()
# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 20)
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'skupina')
worksheet.write('A2', 'World')
print("excel created") 
chcekAndSend()
workbook.close()