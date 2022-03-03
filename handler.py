import base64
import json
import boto3

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    print(event)
    s3_bucket_name = event["pathParameters"].get('bucket')
    s3_object_key = event["queryStringParameters"].get('key')
    file_content = s3_client.get_object( Bucket=s3_bucket_name, Key=s3_object_key)["Body"].read()
    print(file_content)
      # TODO implement
    return {
        'statusCode': 200,
        'headers':{ "Content-Type": "image/jpg" ,
        'Access-Control-Allow-Origin': '*'
         },
        'body': base64.b64encode(file_content).decode('utf-8'),
        'isBase64Encoded': True
    }
