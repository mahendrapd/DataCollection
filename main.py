from bs4 import BeautifulSoup
import requests
'''
url = "www.google.com/index.html"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup.title)
for link in soup.find_all('a'):
    print(link.get('href'))
'''
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "House cost"

for j in search(query, tld="com", num=10, stop=100, pause=2):
    print(j)