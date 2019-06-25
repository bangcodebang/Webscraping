from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import hashlib
import requests
import bs4
browser = webdriver.Chrome('/home/rohit/Downloads/chromedriver')

def open_browser_function( ):

    browser.get('https://www.magicbricks.com')
    browser.implicitly_wait(5)

def front_page_access( ):

    ele = browser.find_element_by_class_name('cityLocProjectField')
    ele.send_keys("Mumbai")
    browser.implicitly_wait(30)
    ele.send_keys(Keys.ENTER)
    browser.implicitly_wait(30)

def back_page_access( ):

    browser.implicitly_wait(50)
    browser.find_element_by_xpath('//*[@id="btnPropertySearch"]').click()

def the_hash_cov(r):

    res = requests.get(r)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    h = []
    for i in soup.select('.flex relative clearfix m-srp-card__container'):
        h.append(i.text)
    #num_add = len(h)
    mumhash = hash(soup.text)
    print("the hash value of the sub webapge of the mumbai section of magicbricks is :", mumhash)
    return mumhash

def quit_browser():
    browser.close()
    browser.quit()


h=[]
open_browser_function()
front_page_access()
r = browser.current_url
p=hash(r)
while(p == hash(r)):
    browser.implicitly_wait(10)
    back_page_access()
    p=hash(browser.current_url)

r = browser.current_url
print(r)
h.append(the_hash_cov(r))






