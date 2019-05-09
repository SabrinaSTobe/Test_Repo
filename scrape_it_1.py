import requests
from bs4 import BeautifulSoup


test_url='https://www.michaels.com/liquitex-pouring-medium/D016943S.html'
#connecting to url and gets us the html content
response=requests.get(test_url)
# print(response.text)
# print(response.url)

#parse html frm url w/ boosoo and store as object soup
soup= BeautifulSoup(response.text, "html.parser")


#getting name, price, availability. searches parsed html for the elements
name_box= soup.find('h1', attrs={'class':'product-name fetch-for-sp-name clearfix'})
#orig_price_box=soup.find('div',attrs={'class':'price-standard dsp'}) #--> add in some bit that says if orig_price_box (or any of the prices) returns 'NoneType' either ignore it or say "There's been a price change"
price_box_1 = soup.find('div', attrs={'class':'product-sales-price'})
price_box_2=soup.select("#product-details-update > div.product-sticky-header.hide > div > div.header-right > div > div.product-pricing > div.product-sales-price")
avail_box= soup.find('button',attrs={'id':'add-to-cart'})


name= name_box.text.strip()
price_1= price_box_1.text.strip()
#for some reason proce_box_2 is a list of len 1, so we need to get that element and convert to text
price_2_test= price_box_2.pop()
price_2=price_2_test.text.strip()
#orig_price=orig_price_box.text.strip()

avail=avail_box.text.strip() 

# #this accomplishes what price_2 was attempting to do. But since there's only one element in price_box_2, "AttributeError: 'list' object has no attribute 'text'"" shouldnt be appearing?
# for i in price_box_2:
#     print (i.text.strip())

print("\nProduct title: "+name)
#print("\nOriginal price found with attr: "+ orig_price)
print("\nPrice found using attr: " + price_1)
print("\nPrice found with CSS selector: " +price_2)
#print(price_box_2)
print("\nAvailability: " +avail)