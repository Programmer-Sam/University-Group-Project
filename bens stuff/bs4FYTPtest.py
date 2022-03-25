from xml.dom.minidom import Element
from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.designmynight.com/manchester/restaurants-in-manchester-city-centre').text
soup = BeautifulSoup(source, 'lxml')

name = soup.find_all('div', class_='card__title-container')
rating = soup.find_all('div', class_='rating')
image = soup.find_all('figure', class_='card__image margin-top-15 margin-bottom-20 col-xs-12')
text_description = soup.find_all('div', class_='card__description margin-top-15')
print(name[0].h3.a.text)
#print(rating[1].text)
print(rating[0].span.text)
#print(text_description[1].p.text)
print(image[0].a.href)
