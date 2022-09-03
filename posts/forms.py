from django import forms
from django.forms import ModelForm
from .models import Post,Category,Schedule

class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=('imagelink','message','category')

        widgets={
            'imagelink': forms.URLInput(attrs={'class':'form-control','placeholer':'Enter Image Link'}),
            'message':forms.Textarea(attrs={'class':'form-control','placeholer':'Enter The Post Description'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }
class DateTimeInput(forms.DateTimeInput):

    input_type='datetime-local' 
    #input_class='form-control'

class ScheduleForm(ModelForm):
    date_to_publish=forms.DateTimeField(widget=DateTimeInput(attrs={'class':'form-control '}))
    class Meta:
        model=Schedule
        fields=('imagelink','design_link','message','category','scheduled_by','date_to_publish','timezone','access_token')

        widgets={
            'imagelink': forms.URLInput(attrs={'class':'form-control','placeholer':'Enter Image Link'}),
            'design_link': forms.FileInput(attrs={'class':'form-control','placeholer':'Enter Image Link'}),
            'message':forms.Textarea(attrs={'id':'emojionearea2','class':'form-control','placeholer':'Enter The Post Description'}),
            'timezone':forms.TextInput(attrs={'class':'form-control','value':'','id':'timezone', 'type':'hidden'}),
            'access_token':forms.TextInput(attrs={'class':'form-control','value':'','id':'access-token','type':'hidden'}),
            'scheduled_by':forms.TextInput(attrs={'class':'form-control','value':'','id':'username', 'type':'hidden'}),
            'category':forms.Select(attrs={'class':'form-control'}),
        }
        