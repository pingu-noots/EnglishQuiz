from typing import Text
import requests
from bs4 import BeautifulSoup
import os
import pprint
import lxml

#url = 'https://gogakuru.com/english/phrase/genre/160_%E9%AB%98%E6%A0%A1%E7%94%9F%E5%90%91%E3%81%8D.html?pageID=1&perPage=50'
url1 = 'https://gogakuru.com/english/phrase/genre/160_高校生向き.html?&pageID=2&layoutPhrase=0&perPage=50'
url2 = 'https://gogakuru.com/english/phrase/genre/160_高校生向き.html?pageID=2&flow=enSearchGenre&condGenre=160&orderPhrase=0&layoutPhrase=0&condMovie=0&perPage=50'
url3 = 'https://gogakuru.com/english/phrase/genre/160_高校生向き.html?pageID=3&orderPhrase=0&layoutPhrase=0&condMovie=0&perPage=50&flow=enSearchGenre&condGenre=160'
url = 'https://gogakuru.com/english/phrase/genre/160_高校生向き.html?pageID=4&orderPhrase=0&layoutPhrase=0&condMovie=0&perPage=50&flow=enSearchGenre&condGenre=160'


res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')
#print(soup)
items = soup.find_all('span', class_='font-en')
asdf = []
for item in items:
    asdf.append(item.text)

#print(asdf)



with open('4.txt', 'a') as f:
    f.write(d)

#print(items.text)
#for item in items:
    # print(item)
    #boxes = soup.find_all('table', class_='item_type01')
    #for box in boxes:
        #asdf = box.find('table', class_='font-en')
        #print(asdf)


# 
# boxes = soup.find_all('table', class_='item_type01')
# print(boxes)[0]
# 
# for box in boxes:
#     asdf = box.find('table', class_='font-en')
#     print(asdf)

