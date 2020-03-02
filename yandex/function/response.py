import json

# Empty response helper
def create_empty():
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({}),
        'isBase64Encoded': False
    }

# Text response helper
def create_text(body):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(body),
        'isBase64Encoded': False
    }
