import json

def handler(event, context):

    body = json.loads(event['body'])
    message = body['message']
    chat = message['chat']

    answer = {
           'method': 'sendMessage',
           'chat_id': chat['id'],
           # "reply_to_message_id" : message["message_id"],
           'text' : 'You wrote: ' + message['text']
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(answer),
        'isBase64Encoded': False
    }