import hashlib


def hashing_your_data(s):
    hash1 = hash(s)
    print ("your hashed value is",hash1)

s=''
import requests
import bs4
res=requests.get('https://en.wikipedia.org/wiki/Machine_learning')
soup = bs4.BeautifulSoup(res.text,'lxml')
for i in soup.select('.toctext'):
    s=s + i.text
s.replace(" ", "")
hashing_your_data(s)
print(s)
