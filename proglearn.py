import validators
import requests
from bs4 import BeautifulSoup
# Make a request
url1 = "https://www.magicbricks.com"
url2 = "https://www.99acres.com"
url3 = "KKk"
validators.url(url2)
if validators.url(url2):
    print("Valid URL")
else:
    print("Not valid")
page = requests.get(url2)
soup = BeautifulSoup(page.content, 'html.parser')
title=soup.title.text
print(title)
ad=[]
i=0
for link in soup.find_all('a'):
    ahref=link.get('href')
    ad.append(ahref)
    #print(i,link.get('href'))
    i=i+1
#print(ad)
page1=requests.get(ad[0])
soup1=BeautifulSoup(page1.content, 'html.parser')
for k in soup1.find_all('a'):
    ahref=link.get('href')
    ad.append(ahref)
print(i)
print(len(ad))

'''
top_items = []
products = soup.select('div.thumbnail')
for elem in products:
    print(elem)

print(products)
'''
