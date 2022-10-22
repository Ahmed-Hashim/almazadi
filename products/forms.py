from .models import*
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','description','time_period','price','created_by']
        name=forms.CharField(label="Service Name")
        description=forms.CharField(label="Description")
        time_period=forms.CharField(label="Time Period")
        price=forms.CharField(label="Price")
        created_by=forms.CharField(label="Created by")
        widgets={
            'created_by':forms.TextInput(attrs={'id':'created-by',"type":"hidden",})
        }
class InvoiceForm(forms.ModelForm):
    class Meta:
        model=Invoice
        fields=[
            'customerid',
            'employeeid',
            'note',
            'status',
            'products',
            'paymentTerms',
            'discount_presentage'
        ]
        customerid=forms.CharField()
        employeeid=forms.CharField()
        note=forms.CharField()
        status=forms.CharField()
        products=forms.CharField()
        paymentTerms=forms.CharField()
        discount_presentage=forms.CharField()
        widgets={
            'employeeid':forms.TextInput(attrs={'id':'employeeid',"type":"hidden",})
            
        }
