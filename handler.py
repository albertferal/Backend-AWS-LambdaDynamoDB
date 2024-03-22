import json
import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('favorites')

def add_favorite(event, context):
    data = json.loads(event['body'])
    org_id = data['org_id']
    favorite_org_id = data['favorite_org_id']
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    table.put_item(Item={'org_id': org_id, 'favorite_org_id': favorite_org_id, 'date': current_date})
    return {
        'statusCode': 200,
        'body': json.dumps('Favorite added successfully!')
    }

def list_favorites(event, context):
    response = table.scan()
    items = response['Items']
    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }
