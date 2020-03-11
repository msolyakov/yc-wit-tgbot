from __future__ import absolute_import

import unittest
import json

from yacloud.function import request
from yacloud.function import response
import main

class Test_MainHandler(unittest.TestCase):

    def test_main_text(self):

        test_body = json.loads(r'{"message_id":1,"from":{"id":108929734,"first_name":"Wit","last_name":"Bot","username":"tg-wit-bot","is_bot":true},"chat":{"id":1734,"first_name":"Ivan","type":"private","last_name":"Ivanov","username":"iivanov"},"date":1435296025,"text":"TEST"}')

        req = request.create_post(test_body)
        resp = main.handler(event=req, context={})

        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp["body"])

        resp_body = json.loads(resp["body"])
        self.assertTrue(resp_body["text"] == "TEST")
    
    def test_main_cmd(self):

        test_body = json.loads(r'{"message_id":1,"from":{"id":108929734,"first_name":"Wit","last_name":"Bot","username":"tg-wit-bot","is_bot":true},"chat":{"id":1734,"first_name":"Ivan","type":"private","last_name":"Ivanov","username":"iivanov"},"date":1435296025,"text":"/ver"}')

        req = request.create_post(test_body)
        resp = main.handler(event=req, context={})

        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp["body"])

        resp_body = json.loads(resp["body"])
        self.assertTrue(resp_body["text"] == "v.0.3.0")





