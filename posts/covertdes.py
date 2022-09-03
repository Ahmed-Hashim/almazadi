from tabnanny import filename_only
from PIL import Image, ImageFilter,ImageFont,ImageDraw
import json
import pathlib
import requests
import shutil

adsfile=open('links/ads.json','r')
#filename = link.split('/')[-1]
def downimg(url):
  filename = url.split('/')[-1]
  path = 'links/'+filename#prompt user for file name

  res = requests.get(url, stream = True)

  if res.status_code == 200:
    with open(path,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',path)
  else:
    print('Image Couldn\'t be retrieved')
  
  return path
def deleteoldimg(path):
    file = pathlib.Path('links/1.jpg')
    file.unlink()
def dropShadow( image, offset=(5,10), background=0xffffff, shadow=0x444444, 
                border=(100), iterations=3):
  """
  Add a gaussian blur drop shadow to an image.  
  
  image       - The image to overlay on top of the shadow.
  offset      - Offset of the shadow from the image as an (x,y) tuple.  Can be
                positive or negative.
  background  - Background colour behind the image.
  shadow      - Shadow colour (darkness).
  border      - Width of the border around the image.  This must be wide
                enough to account for the blurring of the shadow.
  iterations  - Number of times to apply the filter.  More iterations 
                produce a more blurred shadow, but increase processing time.
  """
  
  # Create the backdrop image -- a box in the background colour with a 
  # shadow on it.
  totalWidth = image.size[0] + abs(offset[0]) + 2*border
  totalHeight = image.size[1] + abs(offset[1]) + 2*border
  back = Image.open('bg.jpg')
  w,h=back.size
  new_height = totalHeight
  new_width  = new_height * w / h
  back = back.resize((int(float(new_width)), new_height), Image.ANTIALIAS)
  #area = (left, top, right, bot)
  area = (0, 0, totalWidth, totalHeight)
  back = back.crop(area)
  
  # Place the shadow, taking into account the offset from the image
  shadowLeft = border + max(offset[0], 0)
  shadowTop = border + max(offset[1], 0)
  back.paste(shadow, [shadowLeft, shadowTop, shadowLeft + image.size[0], 
    shadowTop + image.size[1]] )
  
  # Apply the filter to blur the edges of the shadow.  Since a small kernel
  # is used, the filter must be applied repeatedly to get a decent blur.
  n = 0
  while n < iterations:
    back = back.filter(ImageFilter.BLUR)
    n += 1
    
  # Paste the input image onto the shadow backdrop  
  imageLeft = border - min(offset[0], 0)
  imageTop = border - min(offset[1], 0)
  back.paste(image, (imageLeft, imageTop))
  
  return back
def layout(name):
  if __name__ == "__main__":
    image = Image.open(name)
    image.thumbnail( (700,700), Image.ANTIALIAS)
    imagen=dropShadow(image, background=0xeeeeee, shadow=0x444444, offset=(0,5))

    w,h=imagen.size
    
    croped=imagen.crop((75, 75 , w-75, h))
    gp=Image.open('google.jpg')
    aps=Image.open('logos.png')
    logo=Image.open('223.png')

    bi=croped.copy()
    logow=logo.size[0]
    logoh = logo.size[1]
    imageLeft = croped.size[0]-logow-25
    imageTop = croped.size[1]-logoh-15
    bi.paste(logo,(croped.size[0]-logo.size[0]-50, 0),logo)  

    place=(int(float(croped.size[0]/2-175)),croped.size[1]-55)
    apple=bi.copy()
    apple.paste(aps,(place),aps)

    # Create piece of canvas to draw text on and blur
    font = ImageFont.truetype("Fonts/stv-bold.ttf", 25)
    blurred = Image.new('RGBA', apple.size)
    draw = ImageDraw.Draw(blurred)
    draw.text((imageLeft/2+60, imageTop+40), text="حمل التطبيق الان", fill='gray' ,font=font, anchor='mm')
    blurred = blurred.filter(ImageFilter.BoxBlur(10))

  # Paste soft text onto background
    apple.paste(blurred,blurred)
    draw = ImageDraw.Draw(apple)
  # font = ImageFont.truetype(<font-file>, <font-size>)
    
  # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((imageLeft/2-25, imageTop+28),"حمل التطبيق الان",(0, 0, 0),font=font)
    apple.save(name)
  return
#downimg('https://cdn.pixabay.com/photo/2010/12/13/10/05/berries-2277__340.jpg')
img=downimg('https://cdn.pixabay.com/photo/2010/12/13/10/05/berries-2277__340.jpg')
layout(img)
deleteoldimg(img)
