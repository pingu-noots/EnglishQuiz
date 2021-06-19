from os import pardir, path
from re import S
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from googletrans import Translator
from nltk.stem.wordnet import WordNetLemmatizer as WNL
from nltk.stem.porter import PorterStemmer as PS
from nltk.stem.lancaster import LancasterStemmer as LS

s = 'machine learning is employed in a range of computing tasks where designing and program explicit algorithms with good performance is difficult or infeasible. Example. Applications include email filtering, detection of network intruders and computer vision. Machine learning is closely related to computational statistics, which also focuses on predictions making through the use of computer. It has strong ties to mathematical optimization, which delivers methods, theory and application domains to the field.'
v ='Have you ever wondered how much it would cost to translate Japanese into English and how much it would cost to translate it? Therefore, for such people, I will introduce the basic knowledge about translation.First, the translation fee is usually calculated based on the number of words (words) in the finished English manuscript. For example, if you translate a 400-character manuscript in Japanese into English, the number of words will be about 200 to 210 words, so you can safely think that it will be half the number of Japanese characters. If you translate 20,000 characters (50 sheets when converted to 400 characters), 200 words x 50 sheets = 10,000 words. Of course, the number of words may increase depending on the case, such as the Japanese manuscript is for a specialized field, or because it is unique to Japan, supplementary explanation is required. I am cat.'


translator = Translator()
trns = translator.translate(s, dest='en').text
wnl = WNL()
ps = PS()
ls = LS()
#print(trns)

part = word_tokenize(trns)
pos = pos_tag(part)
zenbu = []
asdf = []
#print(pos)

for aaa in pos:
    lang_info = []
    #
    # print(aaa)
    # bbb = nltk.pos_tag(aaa)
    iii = wnl.lemmatize(aaa[0])
    if iii != aaa[0]:
        print(iii)
        print(aaa[0])
        print(f'{"!"*40}')
    #print(aaa[0])
    lang_info.append(aaa[0])
    lang_info.append(aaa[1])
    asdf.append(lang_info)
    #
    # print(asdf
    if aaa[0] == '.':
        zenbu.append(asdf)
        asdf = []
        #print(zenbu)
# print(zenbu)
