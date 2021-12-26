import json

class OrderException(Exception):
    pass

def first_step(event, context):
    print(event)
    if event.get('orderId') == None:
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


if __name__ == "__main__":
    data = {'Comment': 'Insert your JSON here', 'items': {'statusCode': 200, 'body': '[{"item": "item1", "price": 3.5, "quantity": 1}, {"item": "item2", "price": 2.0, "quantity": 6}]'}}
    response = second_step(data, None)
    print(response)
    assert response['body'] == 'Order total is:15.5'

    data = {'orderId': 'abc123'}
    response = first_step(data, None)
    response_body = json.loads(response['body'])
    print(response_body)
    assert response_body[0]['item'] == 'item1'
    assert response_body[1]['item'] == 'item2'
    assert response['statusCode'] == 200

    data = {'orderId': '123'}
    try:
        response = first_step(data, None)
        print(response)
    except OrderException:
        pass

    data = {'orderId': '123'}
    try:
        response = first_step(data, None)
        print(response)
    except OrderException:
        pass

    data = {'foobar': '123'}
    try:
        response = first_step(data, None)
        print(response)
    except OrderException:
        pass
