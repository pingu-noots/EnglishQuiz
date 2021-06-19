import sys
import json
from googletrans import Translator
from polyglot.text import Text
import pandas as pd
import pprint

with open('/tmp/2b7a3b56a2e44971bdcbcb8afbc9684c.json') as f:
    jsn = json.load(f)

    aaa = jsn['results']['transcripts'][0]['transcript']

    translator = Translator()
    trns = translator.translate(aaa, dest='en').text
    lang_parts = []
    word = []
    asdf = []
    tokens = Text(trns)
    for token in tokens.pos_tags:
        asdf = []
        asdf.append(token[0])
        asdf.append(token[1])
        word.append(asdf)
        #pos.append(token[1])
        if token[0] == '.':
            lang_parts.append(word)
            word = []
        

    pprint(lang_parts)

#print(lang_parts[10])

aaa = [('Example', 'NOUN'), ('applications', 'NOUN'), ('include', 'VERB'), ('email', 'NOUN'), ('filtering', 'NOUN'), (',', 'PUNCT'), ('detection', 'NOUN'), ('of', 'ADP'), ('network', 'NOUN'), ('intruders', 'NOUN'), ('and', 'CONJ'), ('computer', 'ADJ'), ('vision', 'NOUN'), ('.', 'PUNCT')]
#for a in aaa:
    #print(a[0])