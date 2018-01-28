import bs4
import time
from urllib.request import urlopen
import requests
import termcolor
import sys
import colorama
colorama.init()
from termcolor import colored
from bs4 import BeautifulSoup as soup
discordHeaders = {"User-Agent": "myBotThing (http://www.google.com/, v0.1)", "Content-Type": "application/json", }

#Opening a connection / Grabbing the page
myurl = 'https://shop.exclucitylife.com/collections/all-footwear-exclucity-men'##Sets the url
uclient = urlopen(myurl)##Opens the url and assigns it to a variable
page_html = uclient.read()##Assigns the whole web page to a variable
uclient.close()##Closes the url

page_soup = soup(page_html, "html.parser")#Instantiates the soup using the html formatted webpage
products = page_soup.findAll("div",{"class" : "grid__cell 1/2--handheld-and-up 1/3--desk"}) ##Finds all tags with the product class (Finds all the product tags and compiles into a list)
productcount = len(products)##Number of products on the webpage
print ("Number of products" + str(productcount))

##for product in products:
##	productname = product.img["alt"]

##	price = product.findAll("p", {"class":"product-card-meta product-card-price"})
##	price = price[0].text.strip()

##	print ("productname: " + productname)
##	print ("price: " + price)


def monitor():
	time.sleep(10)
	print (colored( "Sleeping...","cyan"))

	#Opening a connection to compare
	comparemyurl = 'https://shop.exclucitylife.com/collections/all-footwear-exclucity-men'##Sets the url
	compareuclient = urlopen(myurl)##Opens the url and assigns it to a variable
	comparepage_html = uclient.read()##Assigns the whole web page to a variable
	compareuclient.close()##Closes the url

	comparepage_soup = soup(page_html, "html.parser")#Instantiates the soup using the html formatted webpage
	compareproducts = page_soup.findAll("div",{"class" : "grid__cell 1/2--handheld-and-up 1/3--desk"}) ##Finds all tags with the product class (Finds all the product tags and compiles into a list)
	compareproductcount = len(products)##Number of products on the webpage
	print ("Number of products" + str(productcount))

	#If the original product count is not equal to the current product count, grab product name and price and send to discord
	if (compareproductcount != productcount):
		print(colored("New Product Detected!","magenta"))
		newproduct = compareproducts[-1]

		productname = product.findAll("div",{"class": "productOverlayTrigger"})
		productname = productname[0].text.strip()

		##price = newproduct.findAll("p", {"class":"product-card-meta product-card-price"})
		##price = price[0].text.strip()
		print ("Product Name: " + productname)

		body = {
		                    "content": "",
		                    "embeds": [
		                        {
		                            "title": "New Product!",
		                            "description":  ("Product Name: " + productname)
		                        }
		                              ]
		                        }
		r = requests.post('webhook goes here', headers=discordHeaders, json=body)
while True:
	monitor()
