from __future__ import absolute_import

import unittest

from yandex.function import request
from yandex.function import response
import main

class HandlerTest(unittest.TestCase):

    def test_main_handler(self):

        test_body = {
            'message' : {
                'chat': {
                    'id' : '1234'
                },
                'text': 'test'
            }
        }

        req = request.create_post(test_body)
        resp = main.handler(req, {})

        self.assertIsNotNone(resp)
        self.assertIsNotNone(resp["body"])
        self.assertNotIsInstance(resp["body"], type(dict))
        self.assertTrue(resp["body"]) 

        print(resp)


