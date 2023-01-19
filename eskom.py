import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = 'https://www.citypower.co.za/customers/Pages/Load_Shedding_Downloads.aspx'
#Start HTML Session
session = HTMLSession()
response = session.get(url)
#Soup used for scraping
soup = BeautifulSoup(response.content, 'html.parser')
#Searching for elements that start with: style*='color:#ff000 - THis is the red text of what is needed
elements = soup.select("[style*='color:#ff000']")

for ele in elements:
    #Print elemetns that contain string data and not just HTML data
    s = ele.string
    if s != None:
        print(s)
