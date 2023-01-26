import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://github.com/trending')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
repo_page= soup.find('div', class_='Box')
repos= repo_page.find('div', attrs={'class': None})  #error is due to this line only..... please fix this :)
repo_list = repos.find_all('article',class_="Box-row")
print(len(repo_list))

# Open writer with name
file_name = "github_trending_today.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))

# write a new row as a header
f.writerow(['Repo Name', 'Number of Stars'])

for repo in repo_list:
    #------For the repo name and owner--------
    repo_header= repo_list.find('h1')
    repo_a= repo_header.find("a", href=True)
    #-----------------------------------------
    full_repo_name= repo_a["href"]
    # For the stars------------
    repo_div= repo_list.find('div', class_='f6 color-fg-muted mt-2')
    star_a= repo_div.find('a', class_='Link--muted d-inline-block mr-3')
    #--------------------------
    stars = star_a.find('svg', class_='octicon octicon-star').parent.text.strip()
    # strip() all to remove leading and traling white spaces
    # print('developer', developer)
    # print('name', repo_name)


print(full_repo_name)
print('stars', stars)
      # add the information as a row into the csv table
f.writerow([full_repo_name, stars])
