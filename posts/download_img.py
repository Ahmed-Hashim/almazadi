import requests # request img from web
import shutil # save img locally
def dl_img(url):
  filename = 'media/designs/'+str (url.split('/')[-1])
  res = requests.get(url, stream = True)
  if res.status_code == 200:
    with open(filename,'wb') as f:
        shutil.copyfileobj(res.raw, f)
  return filename

dl_img('https://i.natgeofe.com/n/46b07b5e-1264-42e1-ae4b-8a021226e2d0/domestic-cat_thumb_square.jpg')



