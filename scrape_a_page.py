from __future__ import print_function
import datetime
import requests
import pandas
from bs4 import BeautifulSoup
import mysql.connector as mysql

#connecting to mysql db
mydb=mysql.connect(
    host='localhost',
    user='sabrinastobe',
    password='T0bewanken0bi!',
    database='test_it'
)

print(mydb)

#saying that we will be using sql queries
mycursor=mydb.cursor()

#the query to execute
mycursor.execute("SELECT url_id,url,title_selector,price_selector,avail_selector FROM urls_for_testing")
#executing said query
myresult = mycursor.fetchall()

#making a list of all the entries by rows
product_selector_list=[]
for x in myresult:
    txt=x
    product_row=list(txt)
    product_selector_list.append(product_row)

total_results=[]
for i in product_selector_list:
    product_element=i
    results_per_url=[]
    url_id_element=product_element[0]
    results_per_url.append(url_id_element)
    response=requests.get(str(product_element[1]))
    soup= BeautifulSoup(response.text, "html.parser")
    name_box=soup.select(str(product_element[2]))
    if len(name_box)==0:
        name="No title found"
        results_per_url.append(name)
    else:
        name_single=name_box.pop(0)
        name=name_single.text.strip()
        results_per_url.append(name)
    price_box=soup.select(str(product_element[3]))
    if len(price_box)==0:
        price="No price found"
        results_per_url.append(price)
    else:
        price_test= price_box.pop(0)
        price=price_test.text.strip()
        results_per_url.append(price)
    avail_box=soup.select(str(product_element[4]))
    if len(avail_box)==0:
        avail="No availibility found"
        results_per_url.append(avail)
    else:
        avail_single=avail_box.pop(0)
        avail=avail_single.text.strip()
        results_per_url.append(avail)
    timestamp=datetime.datetime.now()
    string_time = timestamp.strftime('%Y-%m-%d %H-%M-%S')
    results_per_url.append(string_time)
    total_results.append(results_per_url)

print(total_results)

#removing old rows from last checked table
mycursor.execute("TRUNCATE TABLE results_last_checked")

#inserting new rows into results_last_checked
sql="INSERT INTO results_last_checked(url_id, product_title, last_price, last_availability, date_last_checked) VALUES(%s,%s,%s,%s,%s)"
insert_rows=mycursor.executemany(sql, total_results)
print(mycursor.rowcount, " lines were inserted")

#commiting changes and closing connection
mydb.commit()
mydb.close()