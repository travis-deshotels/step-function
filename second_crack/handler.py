import json


class OrderException(Exception):
    pass


def first_step(event, context):
    print(event)
    if event.get('orderId') is None:
        raise OrderException('No orderId was provided!')
    if event['orderId'] != 'abc123':
        raise OrderException(f'No record found for recordId: {event["orderId"]}')
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
