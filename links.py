from bs4 import BeautifulSoup
import requests
import csv
t=[]
source = requests.get('https://www.lifelongindiaonline.com/collections/accessories')
soup = BeautifulSoup(source.content, 'lxml')
main = soup.find('ul',class_='nav nav-tabs d-lg-flex')
for link in main.find_all('li',class_='nav-item primary-size position-relative'):
    links = link.a['href']
    if 'https://www.lifelongindiaonline.com/' not in links:
        linkss = f'https://www.lifelongindiaonline.com/{links}'
        t.append(linkss)
print(t)
print(len(t))