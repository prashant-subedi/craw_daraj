import requests
from bs4 import  BeautifulSoup
url = "https://www.daraz.com.np/smartphones/"

#Importing Django Code


import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'daraj.settings'
django.setup()
from  crawl.models import  ProductDetails


while(True):

    page = requests.get(url)
    #print(requests.text)

    soup = BeautifulSoup(page.text,"lxml")

    #sku -gallary is the class name of divs used to contain a single product
    list_of_products = soup.find_all(name="div",attrs='sku -gallery ')
    for product in list_of_products:

        #Brand,Model and Price are both contained in span tag with attributes given below in list

        brand_name = product.find_all('span',limit=2,attrs=['brand','name'])
        price = product.find_all('span', dir = 'ltr')[1]

        print(brand_name[0].string,
                brand_name[1].string,
                price["data-price"])
        data = ProductDetails(brand = brand_name[0].string,
                       name = brand_name[1].string,
                       price = price["data-price"])
        data.save()
        price = product.find_all('div',attr="price-container")
        print("***")

    next = soup.find('a',title="Next")
    if next == None:
        break
    url = next["href"]
    print("Moving to next page")
