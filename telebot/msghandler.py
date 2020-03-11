import json
from telebot import types
from telebot import util
from telebot import bothelper

class MsgHandler():
    def __init__(self, command_callback, text_callback, voice_callback):
        self.command_callback = command_callback
        self.text_callback = text_callback
        self.voice_callback = voice_callback

    def handle_message(self, json_string):
        self.message = types.Message.de_json(json_string)
        
        _content_type = self.message.content_type
        _result_text = None
        
        if _content_type == 'text':
            _text = self.message.text
    
            if util.is_command(_text):
                _cmd = util.extract_command(_text)
                _agrs = util.extract_arguments(_text)
                _result_text = self.command_callback(_cmd, _agrs)
            
            else:
                _result_text = self.text_callback(_text)

        elif _content_type == 'voice':
            _result_text = self.voice_callback()

        # Bot always replies with text message   
        return bothelper.new_message(self.message.chat.id, _result_text) if _result_text else None
