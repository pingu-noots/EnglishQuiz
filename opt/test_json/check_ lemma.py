from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer as WNL

class lemma(object):
    def __init__(self, word):
        self.word = word
        self.lemma_word = ''

    def be_lemma(self):
        wnl = WNL()
        self.lemma_word = wnl.lemmatize(self.word)
 
if __name__ == '__main__':
    print('!!!!!!!!!!!!!')
    aaa = lemma('easily')
    aaa.be_lemma()
    print(aaa.lemma_word)
