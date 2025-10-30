def lambda_handler(event, context):
    """
    Basic AWS Lambda handler that returns a Hello, world! message.

    Args:
        event (dict): Lambda event input.
        context (object): Lambda context object.

    Returns:
        dict: API Gateway-compatible response with hello message.
    """
    return {
        "statusCode": 200,
        "body": "Hello, world!"
    }
