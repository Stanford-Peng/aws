import json
import boto3
import os
from collections import OrderedDict
from boto3.dynamodb.conditions import Key, Attr, And
from functools import reduce


dynamodb = boto3.resource('dynamodb')
TABLE_NAME = 'Image' 


def lambda_handler(event, context):
    
    if event['httpMethod'] == 'POST' :
        table = dynamodb.Table(TABLE_NAME)
        links = []
        data = json.loads(event['body'])
        unique_tags1 =  data["tags"]
        
        #OrderedDict.fromkeys(data['tags'])
        #unique_tags = { each['tags'] : each for each in data }.values()
        
        print(unique_tags1)
        
        # if the tags is empty, there is no need to filter
        if not unique_tags1:
            return {
                'statusCode': 200,
                'body': 
                    json.dumps({
                        "links": links
                        
                    }),
                'headers': {'Access-Control-Allow-Origin': '*'}
            }

        
        # use reduce function to filter on all elements in an array:
        filtered = table.scan(
            FilterExpression=reduce( And, (Attr('tags').contains(v) for v in unique_tags1))

        )
            #  FilterExpression=Attr('tags').contains(unique_tags1)
            #  reduce(And, ([Key(k).eq(v) for k, v in filters.items()]))
            # table = filtered
            #             data = table.scan(
            #     FilterExpression=Attr('names').contains('freddy')
            # )
            # if table.get_item(Key={'tags': tag}) :
            #     ans = table.get_item(Key={'tags': tag})
            #     link = ans['s3-url']
            #     s3_url = "s3://ass2-images/{0}".format(link)
            
        for result in filtered['Items']:
            links.append(result["s3-url"])
            
        return {
            'statusCode': 200,
            'body': 
                json.dumps({
                    "links": links
                    
                }),
            'headers': {'Access-Control-Allow-Origin': '*'}
        }

# https://stackoverflow.com/questions/46616282/dynamodb-query-filterexpression-multiple-condition-chaining-python