import requests
from bs4 import BeautifulSoup

page = requests.get("https://seekingalpha.com/article/4178101-teslas-european-plug-market-share-fell-one-third")
soup = BeautifulSoup(page.content, 'html.parser')
substring = '<p class="p p1">'
summary = []
for item in soup.find_all('p'):
    if substring in str(item):
        break
    summary.append(str(item))