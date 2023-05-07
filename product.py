
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.lifelongindiaonline.com/collections/kitchen/products/healthyfry-air-fryer-1200w-with-2-5l-cooking-pan-capacity-timer-selection-and-fully-adjustable-temperature-control-black-silver')
soup = BeautifulSoup(source.content, 'lxml')

for img in soup.find_all('li',class_='image-item'):
    image = img.img['src']
    if 'https:' not in image:
        prod_img = f'https:{image}'
    print(prod_img)
name = soup.find('h5',class_='ll-color hind-medium')
prod_name = name.text
print(prod_name)
code = soup.find('h6',class_='sku hind-light').text
print(code)
desc = soup.find('span',class_='light-grey-color primary-size d-block w-xl-80').text
print(desc)
feature = soup.find('p',class_='ll-text font-weight-light primary-size').text
print(feature)
