import os
import json
from yacloud.function import response
from telebot import bothelper, msghandler
from wit import withelper

def handler(event, context):
    answer = None
    try:
        body = json.loads(event['body'])
        msgh = msghandler.MsgHandler(handle_command, handle_text, handle_voice)
        answer = msgh.handle_message(body)
    except Exception as ex: 
        if os.environ.get('DEBUG') == 'TRUE':
            answer = 'Error occured: \r\n' + ex.__str__ #TODO: Add logging

    return response.create_text(answer) if answer else response.create_empty()


def handle_command(cmd, args):
    # TODO
    _result = None
    if cmd == 'ver': # Send version by command 
        _result = 'v.0.3.0'
    
    return _result

def handle_text(text):
    # return withelper.prosess_text(text)
    return text

def handle_voice(audio):
    return 'Voice processing will be implemented soon'

