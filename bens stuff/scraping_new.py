from xml.dom.minidom import Element
from bs4 import BeautifulSoup
import requests

source = requests.get('https://confidentialguides.com/guide/the-coolest-places-to-eat-in-manchester/').text #gets the webpage html code
soup = BeautifulSoup(source, 'lxml') #connects bs4 to the webpage 

cards = soup.find_all('article', class_='card')

for card in cards:

  imageurl = card.div.img['data-src']
  name = card.div.div.h3.a.text
  foodtype = span[i].text
  print(imageurl, name, foodtype)


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