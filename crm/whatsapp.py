import requests
import os

import environ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

def send_whatsapp_message(number,message):
    message=message.encode('utf8').decode('iso-8859-1') 
    inctance = env("INCTANCE_WHATSAPP")
    token=env("TOKEN_WHATSAPP")
    url = f"https://api.ultramsg.com/{inctance}/messages/chat"
    payload = f"token={token}&to={number}&body={message}&priority=1&referenceId="
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.json()
def send_whatsapp_img(number,message,imageurl):
    inctance = env("INCTANCE_WHATSAPP")
    token=env("TOKEN_WHATSAPP")
    url = f"https://api.ultramsg.com/{inctance}/messages/image"
    message=message.encode('utf8').decode('iso-8859-1') 
    payload = f"token={token}&to={number}&image={imageurl}&caption={message}&referenceId=&nocache="
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()

def send_whatsapp_pdf(number,message,file_url):
    inctance = env("INCTANCE_WHATSAPP")
    token=env("TOKEN_WHATSAPP")
    url = f"https://api.ultramsg.com/{inctance}/messages/document"
    message=message.encode('utf8').decode('iso-8859-1') 
    file_name=file_url.split('/')[-1]
    payload = f"token={token}&to={number}&filename={file_name}&document={file_url}&referenceId=&nocache="
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()

def send_whatsapp_video(number,message,videourl):
    inctance = env("INCTANCE_WHATSAPP")
    token=env("TOKEN_WHATSAPP")
    url = f"https://api.ultramsg.com/{inctance}/messages/video"
    message=message.encode('utf8').decode('iso-8859-1') 
    payload = f"token={token}&to={number}&video={videourl}&caption={message}&referenceId=&nocache="
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()