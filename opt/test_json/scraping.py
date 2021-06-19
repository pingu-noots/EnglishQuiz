import requests
from bs4 import BeautifulSoup
import os
import pprint
target_url = 'http://ejje.weblio.jp/content'

aaa = [[['Machine', 'NOUN'], ['learning', 'NOUN'], ['is', 'AUX'], ['employed', 'VERB'], ['in', 'ADP'], ['a', 'DET'], ['range', 'NOUN'], ['of', 'ADP'], ['computing', 'NOUN'], ['tasks', 'NOUN'], ['where', 'ADV'], ['designing', 'VERB'], ['and', 'CONJ'], ['programming', 'NOUN'], ['explicit', 'ADJ'], ['algorithms', 'NOUN'], ['with', 'ADP'], ['good', 'ADJ'], ['performance', 'NOUN'], ['as', 'ADV'], ['difficult', 'ADJ'], ['or', 'CONJ'], ['infeasible', 'ADV'], ['.', 'X']], [['Example', 'NOUN'], ['applications', 'NOUN'], ['include', 'VERB'], ['email', 'NOUN'], ['filtering', 'NOUN'], [',', 'PUNCT'], ['detection', 'NOUN'], ['of', 'ADP'], ['network', 'NOUN'], ['intruders', 'NOUN'], ['and', 'CONJ'], ['computer', 'ADJ'], ['vision', 'NOUN'], ['.', 'PUNCT']], [['Machine', 'NOUN'], ['learning', 'NOUN'], ['is', 'VERB'], ['closely', 'ADV'], ['related', 'ADJ'], ['to', 'ADP'], ['computational', 'ADJ'], ['statistics', 'NOUN'], [',', 'PUNCT'], ['which', 'DET'], ['also', 'ADV'], ['focuses', 'VERB'], ['on', 'ADP'], ['predictions', 'NOUN'], ['making', 'VERB'], ['through', 'ADP'], ['the', 'DET'], ['use', 'NOUN'], ['of', 'ADP'], ['computer', 'NOUN'], ['.', 'PUNCT']], [['It', 'PRON'], ['has', 'VERB'], ['strong', 'ADJ'], ['ties', 'NOUN'], ['to', 'ADP'], ['mathematical', 'ADJ'], ['optimization', 'NOUN'], [',', 'PUNCT'], ['which', 'DET'], ['delivers', 'VERB'], ['methods', 'NOUN'], [',', 'PUNCT'], ['theory', 'NOUN'], ['and', 'CONJ'], ['application', 'NOUN'], ['domains', 'NOUN'], ['to', 'ADP'], ['the', 'DET'], ['field', 'NOUN'], ['.', 'PUNCT']]]

for a in aaa[0]:
    if a[1] == 'PUNCT':
        continue
    asdf = os.path.join(target_url, (a[0]))
    #print(asdf)
    r = requests.get(asdf)         #requestsを使って、webから取得
    soup = BeautifulSoup(r.text, "html.parser")
    #print(soup.find('span', class_='learning-level-content').text)
    

    try:
        pprint(soup.find('span', class_='learning-level-content').text)
    except:
        print('!')
#for a in soup.find_all('span', class_='learning-level-content'):
 #  print(a)

#print(soup.find('span', class_='learning-level-content').text)

#print(found.text)

