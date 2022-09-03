from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import Profile
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=('fullname','bio','profile_pic','phone_number','gender','country','timezone','address','facebook_url','instagram_url','twitter_url','linkedin_url','skype_url','access_token')

        widgets={
            'fullname': forms.TextInput(attrs={'class':'form-control'}),
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'profile_pic':forms.FileInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'country': forms.Select(attrs={'class':'form-control'}),
            'timezone': forms.Select(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class':'form-control'}),
            'skype_url': forms.TextInput(attrs={'class':'form-control'}),
            'access_token': forms.TextInput(attrs={'class':'form-control','type':'password'}),


        }
class UserUpdateForm(forms.ModelForm):
    
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email',  'first_name', 'last_name']   

class PasswordChangingForm(PasswordChangeForm):
    
    old_password=forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1=forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2=forms.CharField(label="Confirm New Password", widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')