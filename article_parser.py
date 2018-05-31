import requests
from bs4 import BeautifulSoup

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
substring = '<p class="p p1">'
summary = []
for item in soup.find_all('p'):
    if substring in str(item):
        break
    summary.append(str(item))