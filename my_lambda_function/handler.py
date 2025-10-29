def lambda_handler(event, context):
    """
    Example Lambda function handler.
    Expects `event` with 'number' key.
    Returns number squared.
    """
    number = event.get("number", 1)
    return {"result": number * number}
