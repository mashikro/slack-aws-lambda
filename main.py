from urllib import request, parse
import json
import os
import random


def send_slack_message(webhook, text):
    compliment = "Hello! You are {text}".format(text=text)
    raw_data = {
        'text': compliment,
        'username': 'mash',
        'icon_emoji': ':unicorn_face:'
    }

    data = json.dumps(raw_data).encode('utf-8')
    req =  request.Request(webhook, data) # this will make the method "POST"
    with request.urlopen(req) as response:
        the_page = response.read()

    
def generate_random_adjective():
    adjectives = ['clever', 'intelligent', 'smart', 'funny', 'cold', 'sour', 'scrawny', 'fluffy', 'pretty']
    return random.choice(adjectives)

def lambda_handler(event, context):

    text = generate_random_adjective() #using AWS Lambda enviroment var
    webhook = os.environ["slack_webhook"]
    send_slack_message(matrix_webhook, text)
 
    return {
        'statusCode': 200,
        'body': json.dumps('Messege sent!')
    }


