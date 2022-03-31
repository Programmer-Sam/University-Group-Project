from xml.dom.minidom import Element
from bs4 import BeautifulSoup
import requests
import db_access as database


source = requests.get('https://confidentialguides.com/guide/the-coolest-places-to-eat-in-manchester/').text #gets the webpage html code
soup = BeautifulSoup(source, 'lxml') #connects bs4 to the webpage 

items = soup.find_all('li', class_='c-Guide_Item')
foodtypes = soup.find_all("span", class_="o-M10 c-Meta c-Meta-lrg")
guideUrls = soup.find_all("a", class_="c-Btn") 

for i in range(len(items)):
  item = items[i]
  imageurl = item.div.img['data-src']
  name = item.div.div.h2.a.text
  guideLink = guideUrls[i]["href"]
  foodtype = foodtypes[i].text

  sourcea = requests.get(guideLink).text #gets the webpage html code
  soupa = BeautifulSoup(sourcea, 'lxml') #connects bs4 to the webpage 

  address = soupa.find_all("address")[0].text
  website = "https://" + soupa.find_all("span", class_="c-Restaurant_ContactLabel")[0].text

  database.AddRestaurant(name, foodtype, address, imageurl, website)
  # print(website, name, foodtype, guideLink, address)


# print(li[1]) #This gets the image URL
# print(li[1]) #this gets the name of the resturaunt 
# print(span[1].text) #this gets the type of food (e.g. European)


# If you want to get the next element then loop through the arrays so 
# the 4th element replace li[1] with li[5] and span[1] with span[5]

# I can also webscrape a description of each resturaunt but im not sure if 
# we would want this so lmk if you want me to do it

# Also make sure you do these pip installs:

# pip3 install beautifulsoup4

# pip3 install lxml

# pip3 install requests 