import os
import json
from yacloud.function import response
from telebot import bothelper
from wit import Wit

def handler(event, context):

    body = json.loads(event['body'])
    input_text = body['message']['text']
    chat_id = body['message']['chat']['id']

    wit_token = os.environ.get('WIT_TOKEN')
    wit_client = Wit(access_token=wit_token)
    answer_text = handle_message(wit_client.message(input_text))

    answer = bothelper.new_message(chat_id, 'v.0.2.0. ' + answer_text) # TODO: Send version by command 
    return response.create_text(answer)


def handle_message(response):
    """
    Customizes our response to the message and sends it
    """
    entities = response['entities']
    # Checks if user's message is a greeting
    # Otherwise we will just repeat what they sent us
    greetings = first_entity_value(entities, 'greetings')
    if greetings:
        text = "Hello!"
    else:
        text = response['_text']
    return text


def first_entity_value(entities, entity):
    """
    Returns first entity value
    """
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

