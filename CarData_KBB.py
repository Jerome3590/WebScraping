#Car Data

from bs4 import BeautifulSoup

import urllib.request as ur
import csv
import re
import os

os.chdir("E:/DAPT/CarMax/")

url = 'http://www.kbb.com/cars-for-sale/cars/?searchtype=new%7cused%7ccertified&distance=none&nr=100&s=yeardesc'
data_page1 = ur.urlopen(url)

soup = BeautifulSoup(data_page1, "lxml")

print(soup.prettify())
print(soup.get_text())
