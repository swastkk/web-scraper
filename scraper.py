import requests
from bs4 import BeautifulSoup

URL= "https://www.python.org/downloads"

req= requests.get(URL)
soup= BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())

