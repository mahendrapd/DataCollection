from bs4 import BeautifulSoup
import requests
try:
    from googlesearch import search
except ImportError:
    print("No module in google search")

query= "president of india"
for j in search(query, tld="com", num=10, stop=10, pause=2):
    print(j)
