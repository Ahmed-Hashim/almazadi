from email.policy import default
from random import choices
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

GENDER=(
    ('Male','Male'),
    ('Female','Female'),
)

TITLE=(
    ('MR','MR'),
    ('MRS','MRS'),
)

# Create your models here.
class Customer(models.Model):
    STATUS=(
        ("Prospect","Prospect"),
        ("Active","Active"),
        ("Expired","Expired"),
        ("Suspended","Suspended"),
    )
    title=models.CharField(max_length=25,choices=TITLE,null=True,blank=True)
    first_name=models.CharField(max_length=120 ,blank=True,null=True)
    middle_name=models.CharField(max_length=120 ,blank=True,null=True)
    last_name=models.CharField(max_length=120 ,blank=True,null=True)
    gender= models.CharField(max_length=10,choices=GENDER,null=True,blank=True)
    lead_referral_source =models.CharField(max_length=120 ,blank=True,null=True)
    industry=models.ForeignKey('Industry',on_delete=models.SET_NULL,null=True,blank=True,related_name='industry_type')
    company=models.CharField(max_length=120 ,blank=False,null=False)
    address=models.CharField(max_length=190,null=True,blank=True)
    street=models.CharField(max_length=190,null=True,blank=True)
    land_phone_number=models.CharField(max_length=20)
    email=models.CharField(max_length=120,null=True,blank=True)
    website=models.CharField(max_length=190,null=True,blank=True)
    Situation= models.CharField(null=True,blank=True ,choices=STATUS,default="Prospect",max_length=100)
    #status= models.ForeignKey('Status',on_delete=models.SET_NULL,null=True,blank=True,related_name='status_type')
    background_info= models.TextField(max_length=500,null=True,blank=True)
    last_contact_date=models.DateTimeField(null=True,blank=True)
    facebook_url= models.CharField(max_length=150,null=True,blank=True)
    instagram_url= models.CharField(max_length=150,null=True,blank=True)
    twitter_url= models.CharField(max_length=150,null=True,blank=True)
    linkedin_url= models.CharField(max_length=150,null=True,blank=True)
    skype_url= models.CharField(max_length=150,null=True,blank=True)
    slug=models.SlugField(("slug"),blank=True,null=True)


    def __str__(self):
        return self.company

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.company)
        super(Customer,self).save(*args,**kwargs)

class Contact(models.Model):
    full_name=models.CharField(max_length=150)
    company=models.ForeignKey(Customer,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=20)
    position=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.company)

class Industry(models.Model):

    name=models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return str(self.name)


class Status(models.Model):

    type=models.CharField(max_length=20,null=True,blank=True)
    
    def __str__(self):
        return str(self.type)
        
class Note(models.Model):
    writer=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.ForeignKey(Customer,on_delete=models.CASCADE)
    notes= models.TextField(max_length=500)
    date=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date']



class Customer_Email(models.Model):
    subject=models.CharField(max_length=50)
    message=models.TextField(max_length=1000)
    file_upload=models.FileField(null=True,blank=True)
    sender=models.ForeignKey(User,on_delete=models.CASCADE )
    company=models.ForeignKey(Customer,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)

    def __str__(self) :
        return '{} ({})'.format(self.company,self.subject)
