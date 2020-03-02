import json

def create_post(body):

    return {
        "httpMethod": "POST",
        # "headers": <словарь со строковыми значениями HTTP-заголовков>,
        # "multiValueHeaders": <словарь со списками значений HTTP-заголовков>,
        # "queryStringParameters": <словарь queryString-параметров>,
        # "multiValueQueryStringParameters": <словарь списков значений queryString-параметров>,
        # "requestContext": <словарь с контекстом запроса>,
        "body": json.dumps(body), # body is an object to request with
        "isBase64Encoded": False
    }