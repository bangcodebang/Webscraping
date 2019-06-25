from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import hashlib
import requests
import bs4
browser = webdriver.Chrome('/home/rohit/Downloads/chromedriver')




def email_cus(s):
    browser.get('http://www.gmail.com')
    r = browser.find_element_by_id('identifierId')
    browser.implicitly_wait(100)
    r.send_keys("prasadrohit239@gmail.com")
    browser.implicitly_wait(100)
    r.send_keys(Keys.ENTER)
    r = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    browser.implicitly_wait(100)
    r.send_keys("bgsirslife")
    browser.implicitly_wait(100)
    r.send_keys(Keys.ENTER)
    r = browser.find_element_by_xpath('//*[@id=":jy"]/div/div')
    r.click()
    browser.find_element_by_xpath('//*[@id=":px"]').send_keys('rohangupta23nov@gmail.com')
    browser.implicitly_wait(100)
    browser.find_element_by_xpath('//*[@id=":qk"]').send_keys('updated on cities'+s)
    browser.implicitly_wait(100)
    browser.find_element_by_xpath('//*[@id=":p5"]').click()

s='none'
email_cus(s)