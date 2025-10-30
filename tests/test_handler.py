from hello_world import lambda_handler

def test_lambda_handler_returns_hello():
    resp = lambda_handler({}, None)
    assert resp["statusCode"] == 200
    assert resp["body"] == "Hello, world!"
