import json
import unittest
from second_crack.handler import first_step, second_step, OrderException


class MyTestCase(unittest.TestCase):
    def test_second_step_happy(self):
        body_data = '[{"item": "item1", "price": 3.5, "quantity": 1}, {"item": "item2", "price": 2.0, "quantity": 6}]'
        data = {'Comment': 'Insert your JSON here', 'items': {'statusCode': 200, 'body': body_data}}
        response = second_step(data, None)
        print(response)
        self.assertEqual(response['body'], 'Order total is:15.5')

    def test_first_step_happy(self):
        data = {'orderId': 'abc123'}
        response = first_step(data, None)
        response_body = json.loads(response['body'])
        print(response_body)
        self.assertEqual(response_body[0]['item'], 'item1')
        self.assertEqual(response_body[1]['item'], 'item2')
        self.assertEqual(response['statusCode'], 200)

    def test_first_step_bad_order_id(self):
        data = {'orderId': '123'}
        try:
            response = first_step(data, None)
            print(response)
        except OrderException as e:
            self.assertEqual(e, 'No record found for recordId: 123')

    def test_first_step_missing_order_id(self):
        data = {'foobar': '123'}
        try:
            response = first_step(data, None)
            print(response)
        except OrderException as e:
            self.assertEqual(e, 'No orderId was provided!')


if __name__ == '__main__':
    unittest.main()
