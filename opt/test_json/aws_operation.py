import time
import boto3
import pandas as pd
import json
import os

transcribe = boto3.client('transcribe')
job_name = "test_tran14"
job_uri = "https://aws-transcript-s3.s3.amazonaws.com/input/transcribe-sample.5fc2109bb28268d10fbc677e64b7e59256783d3c.mp3"
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri':job_uri},
    MediaFormat='mp3',  #wav, mp4, mp3
    LanguageCode='en-US', #'en-US'
    OutputBucketName='aws-transcript-s3',
    OutputKey='en_dir/'+job_name+'.json'
)
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)


#s3 = boto3.resource('s3')
#bucket = s3.Bucket('aws-transcript-s3')
#bucket.download_file(job_name+'.json', '~/opt/json_dir/'+job_name+'.json')
#df = pd.read_json('test_tran10.json')

#print(df['results'][1][0]['transcript'])


