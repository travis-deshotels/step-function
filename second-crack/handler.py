import json


def first_step(event, context):
    print(event)
    items = [
        {
            'item': 'item1',
            'price': 3.5,
            'quantity': 1
        },
        {
            'item': 'item2',
            'price': 2.0,
            'quantity': 6
        }
    ]

    response = {
        'statusCode': 200,
        'body': json.dumps(items)
    }

    return response

def second_step(event, context):
    print(event)

    items = json.loads(event['items']['body'])
    print(items)
    total = 0
    for item in items:
        total += item['price'] * item['quantity']

    response = {
        'statusCode': 200,
        'body': f'Order total is:{total}'
    }

    return response


if __name__ == "__main__":
    data = {'Comment': 'Insert your JSON here', 'items': {'statusCode': 200, 'body': '[{"item": "item1", "price": 3.5, "quantity": 1}, {"item": "item2", "price": 2.0, "quantity": 6}]'}}
    response = second_step(data, None)
    print(response)
    assert response['body'] == 'Order total is:15.5'
