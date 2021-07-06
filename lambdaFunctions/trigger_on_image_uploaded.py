import json
import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
import logging
import object_detection
import base64
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'Image' 


def lambda_handler(event, context):
    # TODO implement
    logging.basicConfig
    logger = logging.getLogger()
    logger.debug('The script is starting.')
    for record in event['Records']:
        
        # get the s3 bucket and ke
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        
        print("File {0} uploaded to {1} bucket".format(key, bucket))
        image = s3_client.get_object(Bucket=bucket, Key=key)
        
        # encode the image in base 64 first then decode in UTF-8 to pass it correctly to the existing object_detection.detect_image
        imageData =  base64.b64encode(image["Body"].read()).decode('utf-8')
        
        #get the tags
        tags = object_detection.detect_image(imageData)
        #location = boto3.client('s3').get_bucket_location(Bucket=bucket_name)['LocationConstraint']
        
        s3_url = "s3://ass2-images-1/{0}".format(key)
        # put the detected tags and s3 url in the dynamodb
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(
           Item={
                's3-url': s3_url,
                'tags' : tags
            }
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Record inserted')
    }