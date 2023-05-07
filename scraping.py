from bs4 import BeautifulSoup
import requests
import csv
csv_file = open('step-lights.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_name','Image Links','Prod_Code','Product Description','Prod_feature'])


source = requests.get('https://www.lifelongindiaonline.com/collections/kitchen/llck-air-fryer/#skip-tags-row')
soup = BeautifulSoup(source.content, 'lxml')

for airlink in soup.find_all('div',class_='product-img-box mb-4'):
    airlinks = airlink.a['href']
    if 'https://www.lifelongindiaonline.com/' not in airlinks:
        airlinkss = f'https://www.lifelongindiaonline.com/{airlinks}'
        
        print(airlinkss)


        source = requests.get(airlinkss)
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
        
        try:
            feature = soup.find('p',class_='ll-text font-weight-light primary-size').text
            print(feature)
            csv_writer.writerow([prod_name,prod_img,code,desc,feature])
        except:
            print('')
            csv_writer.writerow([prod_name,prod_img,code,desc])
    