import unittest
from my_lambda_function.handler import lambda_handler

class TestLambdaHandler(unittest.TestCase):
    def test_square_positive(self):
        event = {"number": 3}
        result = lambda_handler(event, None)
        self.assertEqual(result["result"], 9)

    def test_square_negative(self):
        event = {"number": -4}
        result = lambda_handler(event, None)
        self.assertEqual(result["result"], 16)

    def test_square_default(self):
        event = {}
        result = lambda_handler(event, None)
        self.assertEqual(result["result"], 1)

if __name__ == "__main__":
    unittest.main()
