from bs4 import BeautifulSoup
from random import *

import tweepy
import requests
import time
import difflib

from pip._vendor.distlib.compat import raw_input

#url = raw_input("Enter website to monitor: ")
t = int(raw_input("Wait time: "))
auth = tweepy.OAuthHandler("1ueacMqiMRFtgiB31g0e9BYbm", "pjP9FsGIE3qfTXBNTe1WDeqhaNUvASQgJPBfUTf5GLYIbWzbHM")
auth.set_access_token("820756909166919684-UawRTAQM7CBmploaO0WHOysrNmEr81e", "b2tGu4DyWGX8OmetEF7RYQfE4aPsktpg92nS1owMdvzVW")
api = tweepy.API(auth)

api.update_status("NOW MONITORING RAYSOLES SHOP" + " (" + str(randint(1, 200)) + ")")

while True:
    r1 = requests.get("https://raysoles.org/shop")
    data1 = r1.text
    soup1 = BeautifulSoup(data1, "html.parser")

    time.sleep(t)

    r2 = requests.get("https://raysoles.org/shop")
    data2 = r2.text
    soup2 = BeautifulSoup(data2, "html.parser")

    if soup1 == soup2:
        print("No new items!")
    else:
        print("RAY SOLES SHOP UPDATED!!")
        web = requests.get("http://raysoles.org/shop")
        soup = BeautifulSoup(web.content, "html.parser")
        #links = soup.find_all("a")

        for tag in soup.find_all('a', {'class': 'woocommerce-LoopProduct-link'}, href=True):
            products = tag['href']
            print(products)

        r3 = requests.get(products)
        data3 = r3.text
        soup3 = BeautifulSoup(data3, "html.parser")

        for tag in soup3.find_all(class_="product"):
            print(tag.get('id'))

            id = (tag.get('id'))[8:]

        title = soup3.title.string
        cart = "http://raysoles.org/cart/?add-to-cart=" + id
        print(cart)
        print(title)

        api.update_status("New item: " + title + ". Add to cart: " + cart + " (" + str(randint(1, 300)) + ")")

        #for link in links:
            #print("<a href='%s'>%s</a>)" % (link.get("href"), link.text))

        #item_data = soup.find_all("ul", {"class": "products"})

        #print(item_data)




        



