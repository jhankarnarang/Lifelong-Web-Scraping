from bs4 import BeautifulSoup
import requests
import csv
t = []
source = requests.get('https://www.lifelongindiaonline.com/collections/kitchen/llck-air-fryer/#skip-tags-row')
soup = BeautifulSoup(source.content, 'lxml')

for airlink in soup.find_all('div',class_='product-img-box mb-4'):
    airlinks = airlink.a['href']
    if 'https://www.lifelongindiaonline.com/' not in airlinks:
        airlinkss = f'https://www.lifelongindiaonline.com/{airlinks}'
        t.append(airlinkss)
        print(airlinkss)

#pager = soup.find('div',class_='pagination pagination-boxX')
pagination = soup.find('span',class_='next').a['href']
if 'https://www.lifelongindiaonline.com/' not in pagination:
        next_page = f'https://www.lifelongindiaonline.com/{pagination}'

        print(next_page)

