# Define handler logic and Lambda function
def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": '<img src="https://cultofthepartyparrot.com/parrots/hd/revolutionparrot.gif">',
    }
