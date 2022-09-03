import requests
import base64
import os
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
def uploadimg(file_name):
    MEDIA_ROOT = os.path.join(BASE_DIR,'media')
    filename=MEDIA_ROOT+"/"+file_name
    with open( filename, "rb") as image_file :
        data = base64.b64encode(image_file.read())
    params = {
    'expiration': '600',
    'key': '8333f9583fc7022e902274c574288424',
    }

    files = {
        'image': (None, data.decode('utf-8')),
    }

    response = requests.post('https://api.imgbb.com/1/upload', params=params, files=files)
    json_data=response.json()

    urltofacebook=json_data['data']['image']['url']
    deleteurl=json_data['data']['delete_url']

    return urltofacebook,deleteurl

