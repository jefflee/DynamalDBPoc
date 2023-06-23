import boto3
import uuid

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table('gss')


def create_and_delete_user():
    user_id = str(uuid.uuid4())
    item = {
        "pk": "CUSTOMER#" + user_id,
        "sk": "PROFILE#" + user_id,
        "profile_data": {
            "Some": "stuff"
        }
    }
    response = table.put_item(
        ReturnConsumedCapacity='TOTAL',
        Item=item
    )
    print(response)
    response = table.delete_item(
        ReturnConsumedCapacity='TOTAL',
        Key={
            "pk": "CUSTOMER#" + user_id,
            "sk": "PROFILE#" + user_id
        }
    )
    print(response)


def overload():
    while True:
        create_and_delete_user()


overload()