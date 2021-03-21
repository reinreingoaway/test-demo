import json
import boto3
import random
from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute
)

def add(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_instance = dynamodb.Table('something-table')
    response = {}
    event_body = json.loads(event["body"])

    event_body["something_id"] = f"{random.randint(1, 10000)}"
    event_body["date"] = f"{datetime.now()}"

    if ('something' not in event_body):
        return {
            "statusCode": 400,
            "body": "Wala ka nilagay input hmp"
        }
    try:
        table_instance.put_item(
            Item=event_body
        )
        body = json.dumps(event_body)
        response = {
            "statusCode": 201,
            "body": f"Naadd na puh: {body}"
        }
    except:
        response = {
            "statusCode": 500,
            "body": "Di puh naadd"
        }
    return response

