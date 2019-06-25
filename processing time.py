from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import pandas
import time
import openpyxl
from matplotlib import pyplot as plt

browser = webdriver.Chrome("/home/rohit/Downloads/chromedriver")
k = []
df = pandas.read_csv(r"/home/rohit/Downloads/Cities1.csv")
for i in range(10):
    data = df['Name'][i]
    k.append(data)


def open_function():
    browser.get("https://www.magicbricks.com")
    browser.implicitly_wait(5)


z=[]
open_function()
for i in range(len(k)):
    s = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName='
    s = s + k[i]
    start = time.time()
    browser.get(s)
    end = time.time()
    p = (end - start)
    z.append(p)
print(z)


plt.plot(k,z)
plt.show()
