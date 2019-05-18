import requests
import pandas
from itertools import zip_longest
import csv
from bs4 import BeautifulSoup


colnames=['url_id','urls', 'title_selector', 'price_selector','availibility_selector']
data=pandas.read_csv('url_defs_for_test.csv', names=colnames)
url_ids=data.url_id.tolist()
urls=data.urls.tolist()
title_def=data.title_selector.tolist()
price_def=data.price_selector.tolist()
avail_def=data.availibility_selector.tolist()


for (a,b,c,d) in zip_longest(urls, title_def, price_def, avail_def):
    response=requests.get(str(a))
    soup= BeautifulSoup(response.text, "html.parser")
    name_box_2=soup.select(str(b))
    name_2_single=name_box_2.pop()
    name_2=name_2_single.text.strip()
    price_box_2=soup.select(str(c))
    price_2_test= price_box_2.pop()
    price_2=price_2_test.text.strip()
    avail_box_2=soup.select(str(d))
    avail_2_single=avail_box_2.pop()
    avail_2=avail_2_single.text.strip()
    print("\n\nProduct title: "+name_2)
    print("\nPrice found: " +price_2)
    print("\nAvailability: " +avail_2)

