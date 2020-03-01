import json

def handler(event, context):

    # name = 'World'
    #if 'queryStringParameters' in event and 'name' in event['queryStringParameters']:
    #    name = event['queryStringParameters']['name']

    body = json.loads(event["body"])

    answer = {
           "method": 'sendMessage',
           "chat_id": body.message.chat.id,
           # "reply_to_message_id" : message["message_id"],
           "text" : body.message.text
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(answer),
        'isBase64Encoded': False
    }