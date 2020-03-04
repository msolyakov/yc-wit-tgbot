import json
from yacloud.function import response
from telebot import bothelper

def handler(event, context):

    body = json.loads(event['body'])
    message = body['message']
    chat = message['chat']

    answer = bothelper.new_message(chat['id'], 'v.0.1.2: ' + message['text']) # TODO: Send version by command 
    return response.create_text(answer)