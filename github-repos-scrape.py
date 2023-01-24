import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://github.com/trending')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# get the repo list
repos = soup.find(class_="Box-row")
# For the stars------------
repo_div= repos.find('div', class_='f6 color-fg-muted mt-2')
star_a= repo_div.find('a', class_='Link--muted d-inline-block mr-3')
#--------------------------
# For the Repo name and owner
repo_header= repos.find('h1')
name_a= repo_header.find('a['href']')
print(len(repos))

# Open writer with name
file_name = "github_trending_today.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))

# write a new row as a header
f.writerow(['Developer', 'Repo Name', 'Number of Stars'])

for repo in repos:
    # find the first <a> tag and get the text. Split the text using '/' to get an array with developer name and repo name
    
    # full_repo_name = repo_head.find('a['href']').text.split('/')
    # extract the developer name at index 0
   # developer = full_repo_name[0].strip()
    # extract the repo name at index 1
    # repo_name = full_repo_name[1].strip()
    # find the first occurance of class octicon octicon-star and get the text from the parent (which is the number of stars)
    stars = star_a.find('svg', class_='octicon octicon-star').parent.text.strip()
    # strip() all to remove leading and traling white spaces
  #  print('developer', developer)
   # print('name', repo_name)
    print('stars', stars)
    print('Writing rows')
    # add the information as a row into the csv table
    f.writerow([developer, repo_name, stars])
