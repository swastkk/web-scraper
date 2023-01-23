import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import bs4

url= "https://github.com/swastkk?tab=repositories"
page= requests.get(url)
soup= bs4.BeautifulSoup(page.content, 'html.parser')
lists= soup.find_all('h3', class_='wb-break-all') # used the underscore to have the class as css class not a python class

for list in lists:
    title= list.find('a').text
    status= list.find('span', class_='Label Label--secondary v-align-middle ml-1 mb-1').text
    desc= list.find('p', class_='Label Label--secondary v-align-middle ml-1 mb-1').text
    language= list.find('span', itemprop_='programmingLanguage').text
    last_updated= list.find('relative-time', class_='no-wrap').text
    if_forked= list.find('span', 'a', class_='f6 color-fg-muted mb-1').text
    info=[title, status,desc, language, last_updated, if_forked]

print(info)
