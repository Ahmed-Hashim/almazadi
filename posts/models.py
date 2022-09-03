from statistics import mode
from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class Post(models.Model):
       imagelink = models.URLField(max_length=250)
       design_link= models.ImageField(null=True,blank=True,upload_to="images/designs/")
       message=models.TextField(max_length=1000)
       date=models.DateTimeField(auto_now=True)
       category=models.ForeignKey('Category',on_delete=models.CASCADE)
       published=models.BooleanField(default='False')
       design=models.BooleanField(default='False')
       
       class Meta:
              ordering = ('id',)



class Category (models.Model):
       name=models.CharField(max_length=15)
       def __str__(self):
              return self.name

class Schedule(models.Model):
       imagelink = models.URLField(max_length=250)
       design_link= models.ImageField(null=True,blank=True,upload_to="images/designs/")
       message=models.TextField(max_length=1000)
       date_to_publish=models.DateTimeField(null=True,blank=True)
       category=models.ForeignKey('Category',on_delete=models.CASCADE)
       schedule=models.BooleanField(default='False')
       published=models.BooleanField(default='False')
       timezone=models.CharField(max_length=150,null=True,blank=True)
       access_token=models.CharField(max_length=250,null=True,blank=True)
       scheduled_by=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
       class Meta:
        ordering = ('date_to_publish',)


class PublishedPost(models.Model):
       link = models.URLField(null=True,blank=True,max_length=250)
       imagelink = models.ImageField(null=True,blank=True,upload_to="images/designs/")
       message=models.TextField(max_length=1000)
       category=models.ForeignKey('Category',on_delete=models.CASCADE)
       published_date=models.DateTimeField(null=True,blank=True)
       scheduled_by=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
       fblink=models.URLField(max_length=100,null=True,blank=True)
       fb_post_id=models.CharField(max_length=40,null=True,blank=True)
       class Meta:
        ordering = ('-published_date',)





