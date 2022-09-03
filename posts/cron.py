from posts.views import published_list
from .models import Schedule,PublishedPost
from datetime import datetime
from .uploadtofacebook import *
from pytz import timezone as tz
from .uploadimg import uploadimg
import requests

    


def mada():
    posts=Schedule.objects.filter(schedule=True)
    for i in posts:
        pub_date=i.date_to_publish.strftime('%Y-%m-%d %H:%M:%S')
        if not i.published:
            if pub_date < datetime.now(tz(i.timezone)).strftime('%Y-%m-%d %H:%M:%S'):
                post=Schedule.objects.filter(pk=int(i.id)).values('design_link','message','access_token')
                link=post[0]['design_link']           
                uimagelink=uploadimg(link)
                message=post[0]['message']
                access_token=post[0]['access_token']
                #print(x[1],x[0])
                x= uptofb(uimagelink[0],message,access_token)
                fb='https://facebook.com/'
                post_id=x['post_id']
                #message=str(x)
                #time=f"now={datetime.now(tz(i.timezone)).strftime('%Y-%m-%d %H:%M:%S')},data={pub_date}"
                i.published=True
                i.save()
                PublishedPost.objects.create(imagelink=post[0]['design_link'] ,
                                                message=message,
                                                category_id=i.category_id,
                                                published_date=datetime.now(tz(i.timezone)).strftime('%Y-%m-%d %H:%M:%S'),
                                                scheduled_by=i.scheduled_by,
                                                fb_post_id=post_id,
                                                fblink=fb+post_id)