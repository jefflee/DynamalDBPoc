import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "basicSongsTable"

# -------------------------------------
# Creating a DynamoDB *client* for use:
dynamodb_client = boto3.client('dynamodb', region_name="us-east-1")

# Use the DynamoDB client get item method to get a single item
response = dynamodb_client.get_item(
    TableName=TABLE_NAME,
    Key={
        'artist': {'S': 'Arturus Ardvarkian'},
        'song': {'S': 'Carrot Eton'}
    }
)
print(response['Item'])

# Use the DynamoDB client query method to get songs by artist Arturus Ardvarkian
response = dynamodb_client.query(
    TableName=TABLE_NAME,
    KeyConditionExpression='artist = :artist',
    ExpressionAttributeValues={
        ':artist': {'S': 'Arturus Ardvarkian'}
    }
)
print(response['Items'])

# Use the DynamoDB client query method to get songs by artist Arturus Ardvarkian
# that start with "C"
response = dynamodb_client.query(
    TableName=TABLE_NAME,
    KeyConditionExpression='artist = :artist AND begins_with ( song , :song )',
    ExpressionAttributeValues={
        ':artist': {'S': 'Arturus Ardvarkian'},
        ':song': {'S': 'C'}
    }
)
print(response['Items'])

# Use the DynamoDB client scan operation to retreive all items of the table
dynamodb_client.scan(
    TableName=TABLE_NAME
)
print(response['Items'])

# Note that all Items from the client results above contain the data type descriptors
# E.g. They follow the format 'artist': {'S': 'Name of the Artist'}
# That is not the case for the results of the Table resource operations below


# --------------------------------------------
# Creating a DynamoDB *Table resource* for use
dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)

# Use the DynamoDB Table resource get item method to get a single item
response = table.get_item(
    Key={
        'artist': 'Arturus Ardvarkian',
        'song': 'Carrot Eton'
    }
)
print(response['Item'])

# Use the Table resource to query all songs by artist Arturus Ardvarkian
response = table.query(KeyConditionExpression=Key('artist').eq('Arturus Ardvarkian'))
print(response['Items'])

# Use the Table resource to query all songs by artist Arturus Ardvarkian 
# that start with "C"
response = table.query(KeyConditionExpression=Key('artist').eq('Arturus Ardvarkian') & Key('song').begins_with('C'))
print(response['Items'])

# Use the Table resource to scan table for all items
response = table.scan()
print(response['Items'])

# Note that all Items from the Table service resource have no data type descriptors
