import requests
from bs4 import BeautifulSoup

#define url
test_url='https://www.michaels.com/liquitex-pouring-medium/D016943S.html'

#connecting to url and gets us the html content
response=requests.get(test_url)

#parse html frm url w/ boosoo and store as object soup
soup= BeautifulSoup(response.text, "html.parser")


#getting name, price, availability. searches parsed html for the elements
name_box= soup.find('h1', attrs={'class':'product-name fetch-for-sp-name clearfix'})
price_box_1 = soup.find('div', attrs={'class':'product-sales-price'})
price_box_2=soup.select("#product-details-update > div.product-sticky-header.hide > div > div.header-right > div > div.product-pricing > div.product-sales-price")
avail_box= soup.find('button',attrs={'id':'add-to-cart'})

#defining title, prices, and availability as variables
name= name_box.text.strip()
price_1= price_box_1.text.strip()
price_2_test= price_box_2.pop() #when pull html w/ select, treated as list
price_2=price_2_test.text.strip()
avail=avail_box.text.strip() 

#printing variables
print("\nProduct title: "+name)
print("\nPrice found using attr: " + price_1)
print("\nPrice found with CSS selector: " +price_2)
print("\nAvailability: " +avail)
