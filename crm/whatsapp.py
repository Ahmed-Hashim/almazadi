import requests
import os

import environ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
def send_whatsapp_message(number,message):
    message=message.encode('utf8').decode('iso-8859-1') 
    url = env("URL_WHATSAPP")
    token=env("TOKEN_WHATSAPP")
    payload = f"token={token}&to={number}&body={message}&priority=1&referenceId="
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.json()
