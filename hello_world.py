def lambda_handler(event, context):
    """
    Simple AWS Lambda handler that returns a hello message.
    """
    return {"statusCode": 200, "body": "Hello, world!"}
