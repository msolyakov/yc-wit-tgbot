import json
from yandex.function import response

def handler(event, context):

    body = json.loads(event['body'])
    message = body['message']
    chat = message['chat']

    answer = {
           'method': 'sendMessage',
           'chat_id': chat['id'],
           # "reply_to_message_id" : message["message_id"],
           'text' : 'v.0.1: ' + message['text'] # TODO: Add version in debug mode 
    }

    return response.create_text(answer)