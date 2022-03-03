
import logging
import base64
import boto3
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

response  = {
    'statusCode': 200,
    'headers': {
        'Access-Control-Allow-Headers' : 'Content-Type,file-name',
        'Access-Control-Allow-Origin': '*',
        'Content-Type':'application/json'
    },
    'body': ''
}

def lambda_handler(event, context):

    file_name = event['headers']['file-name']
    file_content = base64.b64decode(event['body'])
    
    BUCKET_NAME = 'bucket-ejemplo-s3'

    try:
        ### put_object to put the object 
        s3_response = s3_client.put_object(Bucket=BUCKET_NAME, Key=file_name, Body=file_content)   
        logger.info('S3 Response: {}'.format(s3_response))
        response['body'] = json.dumps('Your file has been uploaded')

        return response

    except Exception as e:
        raise IOError(e)    