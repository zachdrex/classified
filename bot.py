from random import *

import time
from bs4 import BeautifulSoup
import requests
import tweepy
from oauthlib.uri_validate import query

auth = tweepy.OAuthHandler("1ueacMqiMRFtgiB31g0e9BYbm", "pjP9FsGIE3qfTXBNTe1WDeqhaNUvASQgJPBfUTf5GLYIbWzbHM")
auth.set_access_token("820756909166919684-UawRTAQM7CBmploaO0WHOysrNmEr81e", "b2tGu4DyWGX8OmetEF7RYQfE4aPsktpg92nS1owMdvzVW")
api = tweepy.API(auth)

web = requests.get("http://raysoles.org/shop")
soup = BeautifulSoup(web.content, 'lxml')
links = soup.find_all("a")

#site = soup.find_all("a",{"class":"woocommerce-LoopProduct-link woocommerce-loop-product__link"}, "href")



for link in links:
    print("<a href='%s'>%s</a>)" %(link.get("href"), link.text))

item_data = soup.find("a", {'class':'woocommerce-LoopProduct-link'})

print(item_data)

for tag in soup.find_all('a', {'class':'woocommerce-LoopProduct-link'}, href=True):
    products = tag['href']
    print(products)

    #api.update_status("(" + str(randint(1, 300)) + ")" + " New item detected: " + products)

    r1 = requests.get(products)
    data1 = r1.text
    soup2 = BeautifulSoup(data1, "html.parser")

    for tag2 in soup2.find_all(class_="product"):
        print(tag.get('id'))


        id = (tag2.get('id'))[8:]

        title = soup2.title.string
        cart = "http://raysoles.org/cart/?add-to-cart=" + id
        print(cart)
        print(title)

        api.update_status("New item: " + title + ". Add to cart: " + cart + " (" +str(randint(1,300)) + ")")


