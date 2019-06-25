import requests
import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import pandas
import time
import openpyxl
import matplotlib
from matplotlib import pyplot as plt


def quit_browser():
    browser.close()
    browser.quit()






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

quit_browser()
plt.plot(k,z)
plt.savefig("/home/rohit/Documents/storageproject/graph.png")
plt.show()








def email_cus(s):
	browser = webdriver.Chrome("/home/rohit/Downloads/chromedriver")
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
	r = browser.find_element_by_xpath('//*[@id=":k7"]/div/div')
	r.click()
	browser.find_element_by_xpath('//*[@id=":px"]').send_keys('prasadrohit239@gmail.com')
	browser.implicitly_wait(100)
	browser.find_element_by_xpath('//*[@id=":qk"]').send_keys(
		'these are the cities that have an update'+" :-"+s)
	browser.implicitly_wait(100)
	browser.find_element_by_xpath('//*[@id=":p5"]').click()



type = ["", "Multistorey_Apartment",
"Builder_Floor_Apartment",
"Villa"]

j = []
df = pandas.read_csv(r"/home/rohit/Downloads/Cities1.csv")
for i in range(10):
    data = df['Name'][i]
    j.append(data)


n=0
string_2 = ''
for city in j:
	with open('/home/rohit/Documents/storageproject/' + city + '.txt', 'r') as f:
		g = f.readlines()

	for i in range(len(g)):
		g[i] = g[i].replace('\n', '')
		g[i] = int(g[i])
	h =[]
	s = '123'
	string_1 = ''
	for i in s:
		string_1 = 'https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype='
		i= int(i)
		string_1 = string_1 + type[i] + '&cityName=' + city
		print(string_1)
		res = requests.get(string_1)
		soup = bs4.BeautifulSoup(res.text, 'lxml')
		for i in soup.find_all("a", class_="active"):
			l = (i.find("span", itemprop="name").text)
		l = l.split(")")

		l = int(l[0][1:])
		h.append(l)
	k=[]
	for i in range(len(g)):
		if(g[i]==h[i]):
			pass
		else:
			k.append(i)
			n=1
	if(n==1):
		string_2 = string_2 + city + ","

	print("the updates are made in ")
	for i in k:
		print(type[i])

	with open('/home/rohit/Documents/storageproject/'+city+'.txt', 'w') as f:
		for i in h:
			f.write("%s\n" % i)
if(string_2 == ''):
	string_2 = 'none'
	email_cus(string_2)
else:
	email_cus(string_2)