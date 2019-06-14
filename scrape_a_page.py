import datetime
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


pull_prices=[]
pull_titles=[]
pull_avail=[]
pull_time=[]

for (a,b,c,d) in zip_longest(urls, title_def, price_def, avail_def):
    response=requests.get(str(a))
    soup= BeautifulSoup(response.text, "html.parser")
    name_box_2=soup.select(str(b))
    if len(name_box_2)==0:
        name_2="No title found"
        pull_titles.append(name_2)
    else:
        name_2_single=name_box_2.pop()
        name_2=name_2_single.text.strip()
        pull_titles.append(name_2)
    price_box_2=soup.select(str(c))
    if len(price_box_2)==0:
        price_2="No price found"
        pull_prices.append(price_2)
    else:
        price_2_test= price_box_2.pop()
        price_2=price_2_test.text.strip()
        pull_prices.append(price_2)
    avail_box_2=soup.select(str(d))
    if len(avail_box_2)==0:
        avail_2="No availibility found"
        pull_avail.append(avail_2)
    else:
        avail_2_single=avail_box_2.pop()
        avail_2=avail_2_single.text.strip()
        pull_avail.append(avail_2)
    timestamp=datetime.datetime.now()
    pull_time.append(timestamp)
    print("\n\nProduct title: "+name_2)
    print("\nPrice found: " +price_2)
    print("\nAvailability: " +avail_2)
    print(datetime.datetime.now())

print("\n\n")
print(pull_titles)
print(pull_prices)
print(pull_avail)

data['result_title']=pull_titles
data['request_price']=pull_prices
data['request_avail']=pull_avail
data['request_time']=pull_time

data.to_csv('request_checked.csv')