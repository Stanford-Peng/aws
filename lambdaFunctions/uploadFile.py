import json
import boto3
import base64
import uuid

s3 = boto3.client('s3')
import os
def lambda_handler(event, context):
    if event['httpMethod'] == 'POST' : 
        data = json.loads(event['body'])
        name = data['name']
        
        # get the correct postfix
        _ , postfix = os.path.splitext(name)
        
        image = data['file']
        
        # generate an unique id for any uploaded image
        id = uuid.uuid1()
        name = str(id.hex) + postfix
        
        # decode the image to be put in the s3 bucket
        image = image[image.find(",")+1:]
        dec = base64.b64decode(image + "===")
        
        s3.put_object(Bucket='ass2-images-1', Key=name, Body=dec, ACL='public-read', ContentType='mimetype',ContentDisposition='inline')
        
        return {'statusCode': 200, 'body': json.dumps({'s3-url': name}), 'headers': {'Access-Control-Allow-Origin': '*'}}
        
#Reference: https://medium.com/@shresthshruti09/image-upload-on-aws-s3-using-api-gateway-and-lambda-in-python-4039276b7ca7