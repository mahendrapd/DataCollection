from bs4 import BeautifulSoup
import requests
url1='view-source:https://scholar.google.com/citations?user=Y0rJw8IAAAAJ&hl=en'
url2="https://www.99acres.com/"
page = requests.get(url2)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text # gets you the text of the <title>(...)</title>
print(title)
print(soup.body.text)
'''
page_title = soup.title.text
print(page_title)
page_body = soup.body
page_head = soup.head
print(page_title, page_head)
first_h1 = soup.select('h1')[0].text
print(first_h1)
'''
