import json
import boto3
import base64
import uuid
import os
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'Image' 
# s3 = boto3.client('s3')


def lambda_handler(event, context):
    if event['httpMethod'] == 'GET' : 
        table = dynamodb.Table(TABLE_NAME)
        
        # get all rows in db
        response = table.scan()
        data = response['Items']
        
        # use set to filter out the duplicate values
        tags = set()
        # good practive when reading huge amount of data
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

        # get only tags from db rows
        for row in data:
            if row['tags'] is not None:
                for tag in row['tags']:
                    tags.add(tag)
        
        return {'statusCode': 200, 'body': json.dumps({'tags': list(tags)}), 'headers': {'Access-Control-Allow-Origin': '*'}}

