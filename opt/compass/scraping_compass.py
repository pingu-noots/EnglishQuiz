import requests
from bs4 import BeautifulSoup
import os
import pprint
import lxml

target_url = 'https://connpass.com/calendar/?ym=202108'

res = requests.get(target_url)

soup = BeautifulSoup(res.text, 'lxml')

all_events = soup.find_all('div', class_='events')
one_event = []
day_event =[]
month_event = []

for day in all_events:
    day_events = day.find_all('a', class_='Help')
    for aaa in day_events:
        one_event = []
        link = aaa.get('href')
        one_event.extend([aaa.text, link])
        day_event.append(one_event)
    
        #print(one_event)
        #print(aaa.text)
