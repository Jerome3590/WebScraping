from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import numpy
import csv
import re
import os

os.chdir("E:/DAPT/CarMax/")

driver = webdriver.Chrome("C:\\Users\\Jerome\\Anaconda3\\chromedriver.exe")
driver.get("http://www.kbb.com/cars-for-sale/cars/?searchtype=new%7cused%7ccertified&zipcode=&distance=50&s=distanceasc&nr=75&r=181439766592441200#survey")
driver.implicitly_wait(10)
driver.find_element_by_id("selectedZipCode").send_keys("23219")
driver.find_element_by_id("enterzipsubmit").click()
driver.implicitly_wait(20)

soup = BeautifulSoup(driver.page_source, "lxml")

m_data = soup.find_all("a", {"class":"model-name"})
c_data = soup.find_all("a", {"class":"model-count"})

car_models = []
for modelName in m_data:
    car_models.append(modelName.text)

model_counts = []
for modelCount in c_data:
    model_counts.append(modelCount.text.strip('(,'')'))

df = pd.DataFrame(
    {'CarModel': car_models,
     'ModelCounts': model_counts
     }
)

df.set_index('CarModel', inplace=True)
print(df)
#df.to_csv('CarModels.csv')

#driver.find_element_by_id("model-scroll-right").click()
