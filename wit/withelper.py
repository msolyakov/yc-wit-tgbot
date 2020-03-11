import os
from wit import Wit


def prosess_text(input_text):
    wit_token = os.environ.get('WIT_TOKEN')
    wit_client = Wit(access_token=wit_token)
    return handle_text_response(wit_client.message(input_text))


def handle_text_response(response):
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
