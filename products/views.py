import json
from multiprocessing import context
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.core.paginator import Paginator ,EmptyPage

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import QueryDict
# Create your views here.

from .forms import *
from .models import *
from products.models import *
from datetime import datetime,timedelta
#email imports

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail

# Create your views here.
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def product_crud(request):
    return render(request,'products/products.html',{'title':'Product List'})
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def products_list(request):
    products=Product.objects.all()
    return render(request,'products/product_listing.html',{'products':products,'title':'Product List'})
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def add_product(request):
    form=ProductForm
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204,
                    headers={
                            'HX-Trigger': json.dumps({
                                "productChange": None,
                                "showMessage": f"Product has been added successfully.",
                                "close": "close",
                                "type":"bg-dark"
                            })
                        })
    return render(request,"products/productform.html",{'form':form})
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def delete_product(request,id):
    product=get_object_or_404(Product,id=id)
    if request.method=="GET":
        return render(request,"products/delete_product.html",{'product':product})
    if request.method=="DELETE":
        product.delete()
        return HttpResponse(status=204,
                        headers={
                                'HX-Trigger': json.dumps({
                                    "productChange": None,
                                    "showMessage": f"Product has been deleted successfully.",
                                    "close": "close",
                                    "type":"bg-danger"
                                })
                            })
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def edit_product(request,id):
    product=get_object_or_404(Product,id=id)
    form=ProductForm(instance=product)
    if request.method=="PUT":
        data=QueryDict(request.body).dict()
        form=ProductForm(data,instance=product)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204,
                    headers={
                            'HX-Trigger': json.dumps({
                                "productChange": None,
                                "showMessage": f"Product has been edited successfully.",
                                "close": "close",
                                "type":"bg-dark"
                            })
                        })
    return render(request,"products/productform.html",{'product':product,'form':form})



@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def invoice_crud(request):
    return render(request,'products/invoices.html',{'title':'Invoice List'})
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def invoices_list(request):
    invoices=Invoice.objects.all()
    return render(request,'products/invoice_listing.html',{'invoices':invoices,})
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def add_invoice(request):
    form=InvoiceForm
    if request.method=="POST":
        form=InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204,
                    headers={
                            'HX-Trigger': json.dumps({
                                "invoiceChange": None,
                                "showMessage": f"Invoice has been added successfully.",
                                "close": "close",
                                "type":"bg-dark"
                            })
                        })
    return render(request,"products/invoiceform.html",{'form':form})
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def delete_invoice(request,id):
    invoice=get_object_or_404(Invoice,id=id)        
    if request.method=="DELETE":
        invoice.delete()
        return HttpResponse(status=204,
                        headers={
                                'HX-Trigger': json.dumps({
                                    "invoiceChange": None,
                                    "showMessage": f"Product has been deleted successfully.",
                                    "close": "close",
                                    "type":"bg-danger"
                                })
                            })
    return render(request,"products/delete_invoice.html",{'invoice':invoice})
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def show_invoice(request,id):

    invoice=get_object_or_404(Invoice,pk=id)
    products=invoice.products.all()
    if invoice.products.all().count()>0:
        total=0
        for product in products:
            total+=product.price
    if invoice.discount_presentage:
        discount= total*(invoice.discount_presentage)/100
        after_discount=total-discount
        context={
                "invoice":invoice,
                'products':products,
                'total':total,
                'discount':discount,
                'after_discount':after_discount,
            }
        return render(request,"products/show_invoice.html",context)
    else:
        context={
                "invoice":invoice,
                'products':products,
                'total':total,
            }
        return render(request,"products/show_invoice.html",context)




@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def invoice(request,id):
    invoice=get_object_or_404(Invoice,pk=id)
    products=invoice.products.all()
    if invoice.products.all().count()>0:
        total=0
        for product in products:
            total+=product.price
   
    discount= total*(invoice.discount_presentage)/100
    after_discount=total-discount
    products_price=0
    for product in products:
        products_price+=product.price
    context={
            "invoice":invoice,
            'products':products,
            'total':total,
            'discount':discount,
            'after_discount':after_discount,
        }
        
    return render(request,"crm/invoice.html",context)

def set_to_paid(reqeust,id):
    invoice=get_object_or_404(Invoice,id=id)
    if reqeust.htmx:
        products=invoice.products.all()
        for product in products:
            product=get_object_or_404(Product,id=product.id)
            Customer_product.objects.create(product=product,customerid=invoice.customerid,invoiceid=invoice)
        invoice.status ="PAID"
        invoice.save()
        return HttpResponse(status=204,
                            headers={
                                    'HX-Trigger': json.dumps({
                                        "invoiceChange": None,
                                        "productChange": None,
                                        "showMessage": f"Invoice Paid Successfully.",
                                        "close": "close",
                                        "type":"bg-success"
                                    })
                                })
def expiry_products(request):
    products=Customer_product.objects.filter(end_date__range=[datetime.now(),datetime.now()+timedelta(days=10)])
    
    #print(datetime.now(),datetime.now()+timedelta(days=10))
    context={
        'products':products,
        'title':'Expired Products'
    }
    return render(request,"products/expiry_products.html",context) 