import requests
from bs4 import BeautifulSoup
import json
import wget

links = []
url = 'https://archive.org/details/archiveteam-twitter-stream-2017-11'
source_code = requests.get(url, allow_redirects=False)
soup = BeautifulSoup(source_code.text,'html.parser')
a_tags = soup.find_all('a', class_ = 'stealth download-pill')
for a in a_tags:
    links.append('https://archive.org'+a.get('href'))

print(len(links))
count = 1
messed_up_links = []
for x in links:
    print(count,len(links))
    try:
        filename = wget.download(x)
    except:
        messed_up_links.append(x)
    count+=1

print(messed_up_links)