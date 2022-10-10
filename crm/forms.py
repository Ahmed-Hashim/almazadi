from django import forms
from django.forms import ModelForm
from .models import *


class CustomerForm(ModelForm):
    
    class Meta:
        model=Customer
        fields=(
            'title',
            'first_name',
            'middle_name',
            'last_name',
            'gender',
            'lead_referral_source',
            'industry',
            'company',
            'address',
            'street',
            'email',
            'website',
            'status',
            'background_info',
            'facebook_url',
            'instagram_url',
            'twitter_url',
            'linkedin_url',
            'skype_url',
            'land_phone_number',
            )

        widgets={
            'title':forms.Select(attrs={'class':'form-control',"id":"title"}),
            'first_name':forms.TextInput(attrs={'class':'form-control',"id":"firstname"}),
            'middle_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'lead_referral_source':forms.TextInput(attrs={'class':'form-control'}),
            'industry':forms.Select(attrs={'class':'form-control'}),
            'company':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'street':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'website':forms.URLInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'background_info':forms.Textarea(attrs={'class':'form-control'}),
            'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
            'skype_url':forms.TextInput(attrs={'class':'form-control'}),
            'land_phone_number':forms.TextInput(attrs={'class':'form-control'}),
        }
        
class Customer_Email_Form(forms.ModelForm):
    class Meta:
        model=Customer_Email
        fields=['subject','file_upload','message','sender','company']
        subject=forms.CharField(label="Subject")
        file_upload=forms.FileField(label="attatchments")
        message=forms.CharField(label="Message")   
        sender=forms.CharField(label="Sender")
        company=forms.CharField(label="Company")
        widgets={

   
                'sender':forms.TextInput(attrs={'class':'form-control','id':'sender',"type":"hidden" }),
                'company':forms.TextInput(attrs={'class':'form-control','id':'company',"type":"hidden" }),
        }

class Addcontanct(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
        full_name=forms.CharField(label="Full Name")
        position=forms.CharField(label="Position")
        phone_number=forms.CharField(label="Phone Number")
        company=forms.CharField(label="Message")   
        widgets={
            "company":forms.TextInput(attrs={"type":"hidden",'id':'company',})
        }
class Addnote(forms.ModelForm):
    class Meta:
        model=Note
        fields="__all__"
        writer=forms.CharField()
        company=forms.CharField()
        notes= forms.CharField(label="Note")
        widgets={
            "company":forms.TextInput(attrs={'id':'company',"type":"hidden",}),
            "writer":forms.TextInput(attrs={'id':'user',"type":"hidden",})
        }
