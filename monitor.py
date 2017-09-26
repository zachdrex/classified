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
    r1 = requests.get("https://raysoles.org/")
    data1 = r1.text
    soup1 = BeautifulSoup(data1, "html.parser")

    time.sleep(t)

    r2 = requests.get("https://raysoles.org/")
    data2 = r2.text
    soup2 = BeautifulSoup(data2, "html.parser")

    if soup1 == soup2:
        print("No new items!")
    else:
        print("RAY SOLES SHOP UPDATED!!")
        d = difflib.Differ()
        diff = d.compare(soup1, soup2)
        api.update_status("(" + str(randint(1, 200)) + ")" + " New item detected: http://raysoles.org ")




