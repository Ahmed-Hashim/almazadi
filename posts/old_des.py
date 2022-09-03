import requests
from PIL import Image, ImageFilter,ImageFont,ImageDraw
def dropShadow( image, offset=(5,10), background=0xffffff, shadow=0x444444, 
                border=(150), iterations=3):
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
  back = Image.open('posts/static/images/layout/bg.jpg')
  w,h=back.size
  new_height = totalHeight
  new_width  = new_height * w / h
  back = back.resize((int(float(new_width)), new_height), Image.ANTIALIAS)
  #area = (left, top, right, bot)
  area = (0, 0, totalWidth, totalHeight)
  back = back.crop(area)
  

  # Paste the input image onto the shadow backdrop  
  imageLeft = border - min(offset[0], 0)
  imageTop = border - min(offset[1], 0)
  back.paste(image, (imageLeft, imageTop))
  
  return back

def design(link):
    image = Image.open(requests.get(link, stream=True).raw)
    image.thumbnail( (700,700), Image.ANTIALIAS)

    #dropShadow(image).show()
    imagen=dropShadow(image, background=0xeeeeee, shadow=0x444444, offset=(0,5))
    #imagen.show()
    w,h=imagen.size
    
    croped=imagen.crop((75, 75 , w-75, h))
    #gp=Image.open('google.jpg')
    aps=Image.open('posts/static/images/layout/logos.png')
    logo=Image.open('posts/static/images/layout/223.png')
    qr=Image.open('posts/static/images/layout/1.png')

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
    font = ImageFont.truetype("posts/static/fonts/stv-bold.ttf", 25)
    blurred = Image.new('RGBA', apple.size)
    draw = ImageDraw.Draw(blurred)
    #draw.text((imageLeft/2+60, imageTop+40), text="حمل التطبيق الان", fill='gray' ,font=font, anchor='mm')
    blurred = blurred.filter(ImageFilter.BoxBlur(10))

  # Paste soft text onto background
    apple.paste(blurred,blurred)
    draw = ImageDraw.Draw(apple)
  # font = ImageFont.truetype(<font-file>, <font-size>)
    
  # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((imageLeft/2-25, imageTop+28),"حمل التطبيق الان",(0, 0, 0),font=font)
    
    
    
    qr = qr.resize((75,75), Image.ANTIALIAS)
    qr_add=apple.copy()
    logo_w=qr.size[0]
    logo_h=qr.size[1]
    imageLeft1 = croped.size[0]-logo_w-25
    imageTop2 = croped.size[1]-logo_h-15

    qr_add.paste(qr,(imageLeft1,imageTop2),qr)
    name=link.split('/')[-1]
    location='media/images/designs/'+name
    qr_add.save(location)

    