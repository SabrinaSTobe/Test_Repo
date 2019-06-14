import datetime
import requests
import pandas
from itertools import zip_longest
import csv
from bs4 import BeautifulSoup
from numpy import array
from numpy import vstack


data_CSV=pandas.read_csv('url_defs_for_test.csv')
url_ids=data_CSV.url_id.tolist()
urls=data_CSV.urls.tolist()
title_def=data_CSV.title_selector.tolist()
price_def=data_CSV.price_selector.tolist()
avail_def=data_CSV.availibility_selector.tolist()

total_results=[["Url_Id", "Title_found","Last_price","Last_availability","Last_checked"]]
for (a,b,c,d) in zip_longest(urls, title_def, price_def, avail_def):
    results_per_url=[]
    url_id=url_ids.pop(0) # this is bad code bc shortens the list every time rather than just using the next element in the list
    results_per_url.append(url_id)
    response=requests.get(str(a))
    soup= BeautifulSoup(response.text, "html.parser")
    name_box_2=soup.select(str(b))
    if len(name_box_2)==0:
        name_2="No title found"
        results_per_url.append(name_2)
    else:
        name_2_single=name_box_2.pop()
        name_2=name_2_single.text.strip()
        results_per_url.append(name_2)
    price_box_2=soup.select(str(c))
    if len(price_box_2)==0:
        price_2="No price found"
        results_per_url.append(price_2)
    else:
        price_2_test= price_box_2.pop()
        price_2=price_2_test.text.strip()
        results_per_url.append(price_2)
    avail_box_2=soup.select(str(d))
    if len(avail_box_2)==0:
        avail_2="No availibility found"
        results_per_url.append(avail_2)
    else:
        avail_2_single=avail_box_2.pop()
        avail_2=avail_2_single.text.strip()
        results_per_url.append(avail_2)
    timestamp=datetime.datetime.now()
    results_per_url.append(timestamp)
    print("\n\nProduct title: "+name_2)
    print("\nPrice found: " +price_2)
    print("\nAvailability: " +avail_2)
    print(datetime.datetime.now())
    total_results.append(results_per_url)

print(total_results)

data_CSV.to_csv('last_checked.csv')
with open('last_checked.csv', 'w') as f:
    writer= csv.writer(f)
    for i in total_results:
        writer.writerow(i)
