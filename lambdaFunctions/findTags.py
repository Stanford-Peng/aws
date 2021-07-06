import json
import boto3
import base64
import uuid
import object_detection
import os
from boto3.dynamodb.conditions import Key, Attr, And
from functools import reduce

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'Image' 

def lambda_handler(event, context):
    if event['httpMethod'] == 'POST': 
        data = json.loads(event['body'])
        # name = data['name']
        # _ , postfix = os.path.splitext(name)
        
        image = data['file']
        
        image = image[image.find(",")+1:]
        # dec = base64.b64decode(image + "===").decode('utf-8')
        
        # get the tags from posted image
        tags = object_detection.detect_image(image)
        
        if tags is None:
            return {'statusCode': 200, 'body': json.dumps({'links': [], 'tags':[] } ), 'headers': {'Access-Control-Allow-Origin': '*'}}


        # filter links based on the tags
        table = dynamodb.Table(TABLE_NAME)
        filtered = table.scan(
            FilterExpression=reduce( And, (Attr('tags').contains(v) for v in tags))

        )

        links=[]
        for result in filtered['Items']:
            links.append(result["s3-url"])
        
        return {'statusCode': 200, 'body': json.dumps({'links': links,'tags':tags } ), 'headers': {'Access-Control-Allow-Origin': '*'}}
        
#Reference: https://medium.com/@shresthshruti09/image-upload-on-aws-s3-using-api-gateway-and-lambda-in-python-4039276b7ca7