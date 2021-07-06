import json
import urllib.parse
import boto3
import os
dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'Image' 


s3 = boto3.client('s3')


def lambda_handler(event, context):

    if event['httpMethod'] == 'DELETE' : 
        data = json.loads(event['body'])
        name = data['name']
        # _ , postfix = os.path.splitext(name)
        table = dynamodb.Table(TABLE_NAME)
        for n in name:
            
            #delete from S3 bucket
            s3.delete_object(Bucket='ass2-images-1', Key=n)
        
    
            # delete from the table  
            table.delete_item(
                Key={
                    's3-url': "s3://ass2-images-1/{0}".format(n)
                }
            )
    
    return {'statusCode': 200, 'body': json.dumps({'response': 'deleted'}), 'headers': {'Access-Control-Allow-Origin': '*'}}