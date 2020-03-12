from __future__ import absolute_import

import unittest
import json

from yacloud.function import request
from yacloud.function import response
import main

class Test_MainHandler(unittest.TestCase):

    def test_main_text(self):

        message_body = json.loads(r'{"message_id":1,"from":{"id":108929734,"first_name":"Wit","last_name":"Bot","username":"tg-wit-bot","is_bot":true},"chat":{"id":1734,"first_name":"Ivan","type":"private","last_name":"Ivanov","username":"iivanov"},"date":1435296025,"text":"TEST"}')
        test_body = {
            "message": message_body
        }

        req = request.create_post(test_body)
        resp = main.handler(event=req, context={})

        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp["body"])

        resp_body = json.loads(resp["body"])
        self.assertTrue(resp_body["text"] == "TEST")
    
    def test_main_cmd(self):

        message_body = json.loads(r'{"message_id":1,"from":{"id":108929734,"first_name":"Wit","last_name":"Bot","username":"tg-wit-bot","is_bot":true},"chat":{"id":1734,"first_name":"Ivan","type":"private","last_name":"Ivanov","username":"iivanov"},"date":1435296025,"text":"/ver"}')
        test_body = {
            "message": message_body
        }

        req = request.create_post(test_body)
        resp = main.handler(event=req, context={})

        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp["body"])

        resp_body = json.loads(resp["body"])
        self.assertTrue(resp_body["text"].startswith("v.0.3.0"))

    def test_main_cmd(self):

        message_body = json.loads(r'{"message_id":1,"from":{"id":108929734,"first_name":"Wit","last_name":"Bot","username":"tg-wit-bot","is_bot":true},"chat":{"id":1734,"first_name":"Ivan","type":"private","last_name":"Ivanov","username":"iivanov"},"date":1435296025,"text":"/ver"}')
        test_body = {
            "message": message_body
        }

        req = request.create_post(test_body)
        resp = main.handler(event=req, context={})

        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp["body"])

        resp_body = json.loads(resp["body"])
        self.assertTrue(resp_body["text"].startswith("v.0.3.0"))

    def test_main_voice(self):

        message_body = json.loads(r'{"message_id":1,"from":{"id":108929734,"first_name":"Wit","last_name":"Bot","username":"tg-wit-bot","is_bot":true},"chat":{"id":1734,"first_name":"Ivan","type":"private","last_name":"Ivanov","username":"iivanov"},"date":1435296025}')
        message_body["voice"] = json.loads(r'{"duration": 0,"mime_type": "audio/ogg","file_id": "AwcccccccDH1JaB7w_gyFjYQxVAg","file_size": 10481}')
        test_body = {
            "message": message_body
        }

        req = request.create_post(test_body)
        resp = main.handler(event=req, context={})

        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp["body"])

        resp_body = json.loads(resp["body"])
        self.assertTrue(resp_body["text"] == 'Voice processing will be implemented soon')

