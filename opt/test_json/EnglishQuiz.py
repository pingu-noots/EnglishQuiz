import time
import json
import uuid
import os
import sys
import logging
import boto3
import pandas as pd
from googletrans import Translator
from polyglot.text import Text
from botocore.exceptions import ClientError
import requests
from bs4 import BeautifulSoup
import lxml
# for debug
# import pprint

from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer as WNL

BUCKET = 'aws-transcript-s3'

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

class EnglishQuiz(object):

    def __init__(self, voice_file):
        self.lang_parts = []
        self.s3 = boto3.resource('s3').Bucket(BUCKET)
        self.job_name = uuid.uuid4().hex
        self.voice_file = voice_file
        self.count_word = 0

    def upload(self): # 多分これいらん。。。initに置く？labmda?画面側のjs？
        # TODO 方針決める
        self.s3.upload_file(self.voice_file, 'input/'+self.job_name+'.mp3')

    def transcription(self):
        transcribe = boto3.client('transcribe')
        job_uri = 'https://aws-transcript-s3.s3.amazonaws.com/input/'+self.job_name+'.mp3'
        transcribe.start_transcription_job(
            TranscriptionJobName=self.job_name,
            Media={'MediaFileUri':job_uri},
            MediaFormat='mp3',  #wav, mp4, mp3
            LanguageCode='en-US', #'en-US','ja-JP'
            OutputBucketName=BUCKET,
            OutputKey='en_dir/'+self.job_name+'.json'
        )
        while True:
            status = transcribe.get_transcription_job(TranscriptionJobName=self.job_name)
            if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED']:
                print('transcribe is finished!!!!!!!!!!!!')
                self.download_json()
                break
            elif status['TranscriptionJob']['TranscriptionJobStatus'] in ['FAILED']:
                 print('error is happened!')
            else:
                print('Not ready yet...')
                time.sleep(5)

    def download_json(self):
        # client = boto3.client('s3')
        # result = client.list_objects(Bucket=BUCKET, Prefix='en_dir/')
        # if self.job_name+'.json' in result:
            # print('!!!!!!!!!!')
        # else:
            # print('???????????')
        self.s3.Object(bucket_name='aws-transcript-s3', key='en_dir/'+self.job_name+'.json').download_file('/tmp/'+self.job_name+'.json')

    def translate(self):
        while_period = []
        word_in_line = 0
        with open('/tmp/'+self.job_name+'.json') as f:
            jsn = json.load(f)
            before_str = jsn['results']['transcripts'][0]['transcript']
            translator = Translator()
            trns = translator.translate(before_str, dest='en').text
            # 分かち書き
            part = word_tokenize(trns)
            # トークン化したものに品詞タグ付与
            pos = pos_tag(part)
            # tokens = Text(trns) polyglotの場合
            # 単語ごとにループ
            for token in pos:
                word_in_line += 1
                lang_info = []
                level = self.lang_level(token[0], token[1])
                lang_info.append(token[0])
                lang_info.append(token[1])
                lang_info.append(level)
                # 1単語についての情報を文ごとの配列に追加
                while_period.append(lang_info)
                # ピリオドまできたら文ごとの配列を全体配列に格納
                if token[0] == '.':
                    self.lang_parts.append(while_period)
                    while_period = []
                    self.count_word = word_in_line
                    word_in_line = 0
                    


    def lang_level(self, word, pos):
        if word == '.' or word == '-' or word == ',':
            return 0
        wnl = WNL()
        lemma_word = wnl.lemmatize(word)
        weblio_url = 'http://ejje.weblio.jp/content'
        target_url = os.path.join(weblio_url, lemma_word)
        r = requests.get(target_url)         #requestsを使って、webから取得
        soup = BeautifulSoup(r.text, 'lxml')
        try:
            level = soup.find('span', class_='learning-level-content').text
        except:
            return '!'
        return level

if __name__ == '__main__':
    aaa = EnglishQuiz('transcribe-sample.5fc2109bb28268d10fbc677e64b7e59256783d3c.mp3')
    aaa.upload()
    aaa.transcription()
    #aaa.download_json()
    aaa.translate()

    print(aaa.lang_parts)