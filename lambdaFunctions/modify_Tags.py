import json
import boto3
import base64
import uuid
import os
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'Image' 


def lambda_handler(event, context):
    if event['httpMethod'] == 'PUT' : 
        
        
        data = json.loads(event['body'])
        name = data['name']
        # _ , postfix = os.path.splitext(name)
        
        # get the added tags
        tags = data['tags']
        
        # name = url.split('/')[-1]
        
        # format name into s3-url
        s3URL = "s3://ass2-images-1/{0}".format(name)
        print(s3URL)
        
        table = dynamodb.Table(TABLE_NAME)
        
        # update the tags for a data row
        table.update_item(
           Key={
                's3-url': s3URL,
            },
            UpdateExpression="SET tags = list_append(tags, :tags)",
            ExpressionAttributeValues={
                ':tags': tags,
            },
            ReturnValues="UPDATED_NEW"
        )
        
        
        return {'statusCode': 200, 'body': json.dumps({'s3-url': name}), 'headers': {'Access-Control-Allow-Origin': '*'}}
        



# import json

# def lambda_handler(event, context):
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }
