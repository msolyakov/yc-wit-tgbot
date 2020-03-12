import os
import json
from yacloud.function import response
from telebot import bothelper, msghandler
from wit import withelper

def handler(event, context):
    answer = None
    try:
        body = json.loads(event["body"])
        msgh = msghandler.MsgHandler(handle_command, handle_text, handle_voice)
        answer = msgh.handle_message(body["message"])

    except Exception as ex: 
        if os.environ.get('DEBUG'):
            answer = 'Error occured. {}'.format(str(ex))

    return response.create_text(answer) if answer else response.create_empty()


def handle_command(cmd, args):
    _debug = os.environ.get('DEBUG')
    _result = None

    # TODO
    if _debug:
        if cmd == 'debug':
            _result = 'DEBUG {}'.format(args)

    if cmd == 'ver': # Send version by command
        _ver = 'v.0.3.0'
        _result = '{0}, DEBUG = {1}'.format(_ver, _debug) if _debug else _ver
    
    return _result

def handle_text(text):
    # return withelper.prosess_text(text)
    return text

def handle_voice(voice):
    _debug_trace = 'DEBUG file_id = {0}, duration = {1}, mime_type = {2}, file_size = {3}'.format(voice.file_id, voice.duration, voice.mime_type, voice.file_size)
    return _debug_trace if os.environ.get('DEBUG') else 'Voice processing will be implemented soon'

