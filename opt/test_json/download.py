import time
import boto3
import pandas as pd
import json
import os

transcribe = boto3.client('transcribe')
job_name = "foo"
job_uri = "https://aws-transcript-s3.s3.amazonaws.com/input/transcribe-sample.5fc2109bb28268d10fbc677e64b7e59256783d3c.mp3"


s3 = boto3.resource('s3')
bucket = s3.Bucket('aws-transcript-s3')
s3.Object(bucket_name='aws-transcript-s3', key='output2/'+job_name+'.json').download_file('/tmp/'+job_name+'.json')
#bucket.download_file('output2/'+job_name+'.json', 'tmp/'+job_name+'.json')
#df = pd.read_json('test_tran10.json')

#print(df['results'][1][0]['transcript'])


