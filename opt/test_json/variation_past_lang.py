from posixpath import pardir
import requests
from bs4 import BeautifulSoup
import os
import pprint
import lxml

target_url = 'https://toiguru.jp/irregular-verbs'

r = requests.get(target_url)
soup = BeautifulSoup(r.text, 'lxml')

asdf = soup.find_all('table', class_='wp-block-table has-fixed-layout')


moto = []
parts = []
#print(soup.find_all('tr'))
aaa = soup.find_all('tr')
for bbb in aaa:
    for ccc in bbb:
        ddd = ccc.text
        parts.append(ddd)
    moto.append(parts)
    parts = []

print(moto)


    #for ddd in ccc:
    #    eee = ddd.find('td')
        #print(aaa)





    #for ddd in ccc:
     #   eee = ddd.find('td')
      
      #  print(eee)
#print(aaa.find_all('td'))
