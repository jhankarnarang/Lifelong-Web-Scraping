from bs4 import BeautifulSoup
import requests
import csv

m_source = requests.get('https://www.lifelongindiaonline.com/')
m_soup = BeautifulSoup(m_source.content, 'lxml')
m_main = m_soup.find('div',class_='collapse navbar-collapse')
#print(main)

for m_links in m_main.select('li',class_='nav-item'):
    main_links = m_links.a['href']
    print(main_links)