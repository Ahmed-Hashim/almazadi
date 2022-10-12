from datetime import datetime
from django.shortcuts import render,redirect
from .models import Post,PublishedPost,Schedule
from .uploadtofacebook import *
from .forms import PostForm,ScheduleForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
from django.urls import reverse_lazy
from .image_des import *
from .uploadimg import *
from django.contrib import messages
import json
from pytz import timezone as tz

def get_json(request,*args, **kwargs):
   post_lists=Post.objects.all()
   post_published_count=Post.objects.filter(published=True).count()
   post_unpublished_count=Post.objects.filter(published=False).count()
   published_precent=round(post_published_count / post_unpublished_count*100)
   data={
      'name':published_precent
   }
   return JsonResponse(data)

# Create your views here.
@login_required
def dashboard(request):
   link=""
   post_lists=Post.objects.all()
   try:
#Dashboard Chats Data
      post_published_count=Post.objects.filter(published=True).count()
      post_unpublished_count=Post.objects.filter(published=False).count()
      post_count=Post.objects.all().count()
      published_precent=round(post_published_count / post_unpublished_count*100)
      puppost_car=Post.objects.filter(category__name__contains='Car')
      puppost_house=Post.objects.filter(category__name__contains='House')
      puppost_job=Post.objects.filter(category__name__contains='Job')
      puppost_food=Post.objects.filter(category__name__contains='Food')
      puppost_phone=Post.objects.filter(category__name__contains='Phone')
      puppost_school=Post.objects.filter(category__name__contains='School')
      puppost_computer=Post.objects.filter(category__name__contains='Computer')
      puppost_garden=Post.objects.filter(category__name__contains='Garden')
      pub_car=puppost_car.filter(published=True)
      pub_house=puppost_house.filter(published=True)
      pub_job=puppost_job.filter(published=True)
      pub_food=puppost_food.filter(published=True)
      pub_phone=puppost_phone.filter(published=True)
      pub_school=puppost_school.filter(published=True)
      pub_computer=puppost_computer.filter(published=True)
      pub_garden=puppost_garden.filter(published=True)
      unpub_car=puppost_car.filter(published=False)
      unpub_house=puppost_house.filter(published=False)
      unpub_job=puppost_job.filter(published=False)
      unpub_food=puppost_food.filter(published=False)
      unpub_phone=puppost_phone.filter(published=False)
      unpub_school=puppost_school.filter(published=False)
      unpub_computer=puppost_computer.filter(published=False)
      unpub_garden=puppost_garden.filter(published=False)
      context={
         'post_count':post_count,
         'post_published':post_published_count,
         'post_unpublished':post_unpublished_count,
         'precent':published_precent,
         'posts':post_lists,
         'post_count':post_count,
         'post_car':puppost_car.count(),
         'post_house':puppost_house.count(),
         'post_job':puppost_job.count(),
         'post_food':puppost_food.count(),
         'post_phone':puppost_phone.count(),
         'post_school':puppost_school.count(),
         'post_computer':puppost_computer.count(),
         'post_garden':puppost_garden.count(),
         'pub_car':pub_car.count(),
         'pub_house':pub_house.count(),
         'pub_job':pub_job.count(),
         'pub_food':pub_food.count(),
         'pub_phone':pub_phone.count(),
         'pub_school':pub_school.count(),
         'pub_computer':pub_computer.count(),
         'pub_garden':pub_garden.count(),
         'unpub_car':unpub_car.count(),
         'unpub_house':unpub_house.count(),
         'unpub_job':unpub_job.count(),
         'unpub_food':unpub_food.count(),
         'unpub_phone':unpub_phone.count(),
         'unpub_school':unpub_school.count(),
         'unpub_computer':unpub_computer.count(),
         'unpub_garden':unpub_garden.count(),
      }
   except:
      context={}
      
   
   return render (request,'post/dashboard.html',context)

@login_required
def get_posts(request):
   cat=['car','house','job','food','phone','school','computer','garden']
   f=1
   for z in cat:
      file= open(f'./Frontend/links/link{z}.txt','r')
      for i in file:
        messsage="إذا كنت تحتاج إلى عدد أكبر من الفقرات يتيح لك مولد النص العربى زيادة عدد الفقرات كما تريد، النص لن يبدو مقسما ولا يحوي أخطاء لغوية، مولد النص العربى مفيد لمصممي المواقع على وجه الخصوص، حيث يحتاج العميل فى كثير من الأحيان أن يطلع على صورة حقيقية لتصميم الموقع."
        link=i.rstrip()
        myobject = Post(imagelink=link,message=messsage,category_id=f)
        myobject.save() 
      f=f+1

@login_required
def upload(request):
    if request.method == 'POST':
        get_posts(request)
        return redirect("unpublished")
    return render (request,'post/upload.html')

@login_required
def unpublished_list(request):
   
   #paginator
   post_lists=Post.objects.filter(published=False)
   paginator = Paginator(post_lists,8) # Show 25 contacts per page.
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   
   #Update database PUBLISH
   if request.method =='POST' and 'published'in request.POST:
     id_list= request.POST.getlist('boxes')
     for id in id_list:
      Post.objects.filter(pk=int(id)).update(published=True)
      post=Post.objects.filter(pk=int(id)).values('imagelink','message')
      link=post[0]['imagelink']
      message=post[0]['message']
      uptofb(link,message)
     return redirect('published')
     #Update database delete
   if request.method =='POST' and 'delete' in request.POST:
      id_list= request.POST.getlist('boxes')
      for id in id_list:
         Post.objects.filter(pk=int(id)).delete()
      return redirect('unpublished')
   if request.method =='POST' and 'schedule' in request.POST:
      id_list= request.POST.getlist('boxes')
      for id in id_list:
         post=Post.objects.get(pk=id)
         if post.design_link:
            myobject = Schedule(imagelink=post.imagelink,design_link=post.design_link,message=post.message,category_id=post.category_id,timezone="")
         else:
            myobject = Schedule(imagelink=post.imagelink,message=post.message,category_id=post.category_id,timezone="")

         myobject.save()
         post.delete()
      return redirect('schedule_posts')

   context={'posts':page_obj,
   "title":"Unpublished Posts"
              
   }
   return render (request,'post/posts_unpublished.html',context)

@login_required
def published_list(request):
   
   published_list=PublishedPost.objects.get_queryset().order_by('id')
   paginator = Paginator(published_list, 8) # Show 25 contacts per page.
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   context={'posts':page_obj,
            'title':'Published Posts'
              
   }
   
   return render (request,'post/posts_published.html',context)

@login_required
def publish_now(request,id):
   postupdate=Post.objects.filter(pk=int(id))
   post=Post.objects.get(pk=int(id))
   if request.user.profile.access_token:
      if post.design_link: 
      
         link=uploadimg(str(post.design_link))[0]
         print(link)
      else:
         link=post.imagelink
      message=post.message
      access_token=request.user.profile.access_token
      data=uptofb(link,message,access_token)
      postupdate.update(published=True)
      try:
         post_id=data['post_id']
         fb=f'https://facebook.com/{post_id}'
         PublishedPost.objects.create(imagelink=post.design_link,
            link=post.imagelink,
            message=message,
            category_id=post.category_id,
            published_date=datetime.now(tz(request.user.profile.timezone)).strftime('%Y-%m-%d %H:%M:%S'),
            scheduled_by=request.user,
            fb_post_id=post_id,
            fblink=fb+post_id)
         messages.success(request,"Your post has been published")
         return redirect(request.META.get('HTTP_REFERER'))
      except:
         messages.error(request,"Access Token Expired")
         return redirect(request.META.get('HTTP_REFERER'))
   else:
      messages.error(request,"You dont have permissions to publish post")
      return redirect(request.META.get('HTTP_REFERER'))


@login_required
def post_details(request,id):
   post_details=Post.objects.get(id=id)
   if request.method =='POST' and 'publish' in request.POST:
      print(post_details)
      post=Post.objects.filter(pk=int(id)).values('imagelink','message')
      link=post[0]['imagelink']
      message=post[0]['message']
      uptofb(link,message)
      post.update(published=True)
      return redirect(unpublished_list)

   context={'post_details':post_details,
            'title':'Post Details' 
   }
   return render (request,'post/post_detail.html',context)

@login_required
def createpost(request):
   submitted=False
   if request.method=="POST":
      form=PostForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request,"Your post has been added to unpublished list")
         return redirect(unpublished_list)
   else:
      form=PostForm
      if 'submitted' in request.GET:
         submitted=True

   context={'form':form,
            'submitted':submitted,
            'title':'Create Post'  
   }
   return render (request,'post/create_post.html',context)

@login_required
def edit_details(request,id):
   post_details=Post.objects.get(pk=id)
   form = PostForm(request.POST or None,instance=post_details)
   if form.is_valid():
      form.save()
      return redirect("post_details",id)
   context={'post_details':post_details,'form':form,
            'title':'Edit Post' 
              
   }
   return render (request,'post/edit_post.html',context)

@login_required   
def delete_post(request,id):
   post=Post.objects.get(pk=id)
   post.delete()
   messages.info(request,"your post/s has been deleted..")
   return redirect(request.META.get('HTTP_REFERER'))
@login_required   
def delete_schedule(request,id):
   post=Schedule.objects.get(pk=id)
   post.delete()
   #return redirect(request.META.get('HTTP_REFERER'))
   return redirect('schedule_posts')
@login_required
def schedule_posts(request):

   scheduled_list=Schedule.objects.all()
   #paginator = Paginator(published_list,20) # Show 25 contacts per page.
   #page_number = request.GET.get('page')
   #page_obj = paginator.get_page(page_number)
   context={'posts':scheduled_list,
            'title':'Scheduled Post'        
   }
   return render (request,'post/schedule_posts.html',context)

@login_required
def add_to_schedule(request,id):
   post=Post.objects.get(pk=id)
   if post.design_link:
      myobject = Schedule(imagelink=post.imagelink,design_link=post.design_link,message=post.message,category_id=post.category_id,timezone="")
   else:
      myobject = Schedule(imagelink=post.imagelink,message=post.message,category_id=post.category_id,timezone="")

   myobject.save()
   post.delete()
   return redirect('schedule_posts')
@login_required
def edit_schedule_post(request,id):
   post_details=Schedule.objects.get(pk=id)
   form = ScheduleForm(instance=post_details)
   if request.method =='POST':
      form = ScheduleForm(request.POST,request.FILES,instance=post_details)
      if form.is_valid():
         form.save()
         post_details.schedule=True
         post_details.save()
         return redirect('schedule_posts')
   context={'post_details':post_details,'form':form,
              
   }
   return render (request,'post/edit_schedule_post.html',context)

def make_design(request,id):
   post_details=Post.objects.get(pk=id)
   link=post_details.imagelink
   location="images/designs/"+link.split('/')[-1]
   design(link)
   Post.objects.filter(pk=int(id)).update(design_link=location,design=True)
   return redirect(request.META.get('HTTP_REFERER'))
def new_design(request,id):
   post_details=Post.objects.get(pk=id)
   link=post_details.imagelink
   location="images/designs/"+link.split('/')[-1]
   Post.objects.filter(pk=int(id)).update(design_link=location,design=True)
   return redirect(request.META.get('HTTP_REFERER'))
def schedule_design(request,id):
   post_details=Schedule.objects.get(pk=id)
   link=post_details.imagelink
   location="images/designs/"+link.split('/')[-1]
   design(link)
   Schedule.objects.filter(pk=int(id)).update(design_link=location)
   return redirect(request.META.get('HTTP_REFERER'))

def delete_post_ajax(request,id):
   post=Schedule.objects.get(pk=id)
   post.delete()
   return JsonResponse({})

def test(request):
   return render(request,'post/test.html')