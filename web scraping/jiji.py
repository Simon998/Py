import requests
from bs4 import BeautifulSoup
import urllib.request

# send a GET request to the website
response = requests.get('https://jiji.co.ke/nairobi/mobile-phones')

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find all the products on the page
products = soup.find_all('div', class_='item')


for product in products:
    # get the product title
    title = product.find('a', class_='title').text.strip()

    # get the product price
    price = product.find('div', class_='price').text.strip()

    # get the product image URL
    image_url = product.find('img')['src']

    # download the product image
    urllib.request.urlretrieve(image_url, title+'.jpg')

    # print the details
    print(f"Product: {title}")
    print(f"Price: {price}")
    print(f"Image URL: {image_url}")
    print('\n')
