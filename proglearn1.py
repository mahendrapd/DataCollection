import validators
import requests
from bs4 import BeautifulSoup
url1 = "https://www.magicbricks.com"
url2 = "https://www.99acres.com"
page = requests.get(url1)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text
print(title)
ad = []
for link in soup.find_all('a'):
    ahref = link.get('href')
    if ahref is not None:
        if validators.url(ahref):
            ad.append(ahref)

print(len(ad))

'''
vlink = []
for k in range(len(ad)):
    hlink = ad[k]
    if validators.url(hlink):
        vlink.append(hlink)
print(len(vlink))
'''
#print(vlink)
#print(ad[207])
#print(ad[208])
