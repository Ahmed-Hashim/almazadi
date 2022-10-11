from django.shortcuts import render
from .models import *
# Create your views here.
def products_list(request):
    products=Products.objects.all()
    return render(request,'products/products.html',{'products':products})