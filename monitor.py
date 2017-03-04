from bs4 import BeautifulSoup

import tweepy
import requests
import time
import difflib

from pip._vendor.distlib.compat import raw_input

url = raw_input("Enter website to monitor: ")
t = int(raw_input("Wait time: "))

auth = tweepy.OAuthHandler("1ueacMqiMRFtgiB31g0e9BYbm", "pjP9FsGIE3qfTXBNTe1WDeqhaNUvASQgJPBfUTf5GLYIbWzbHM")
auth.set_access_token("820756909166919684-UawRTAQM7CBmploaO0WHOysrNmEr81e", "b2tGu4DyWGX8OmetEF7RYQfE4aPsktpg92nS1owMdvzVW")
api = tweepy.API(auth)

api.update_status("NOW MONITORING: " + url)

while True:
    r1 = requests.get(url)
    data1 = r1.text
    soup1 = BeautifulSoup(data1, "html.parser")

    time.sleep(t)

    r2 = requests.get(url)
    data2 = r2.text
    soup2 = BeautifulSoup(data2, "html.parser")



    if soup1 == soup2:
        print("No Change!")
        #api.update_status("chapo is a bitch")

    else:
        print(url + " has changed!")
        d = difflib.Differ()
        diff = d.compare(soup1, soup2)
        #print('\n'.join(diff))

        api.update_status("CHANGE: " + url)

