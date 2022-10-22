from email import message
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

from products.views import invoice
from .whatsapp import send_whatsapp_img, send_whatsapp_message, send_whatsapp_pdf, send_whatsapp_video
# Create your views here.

from .forms import *
from .models import *
from products.models import *

#email imports

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail








class CustomPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def customerlist(request):

    context={ "customers":Customer.objects.all()  
        }
    
    return render(request,'crm/listing.html',context)

@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@require_http_methods(['POST'])
def AddClient(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"{Customer.objects.first()} Has been added to client list")

    customers=Customer.objects.all()
    context={
        'customers':customers,}
    return  HttpResponse(status=204,
                            headers={
                                'HX-Trigger': json.dumps({
                                "showMessage":' <i class="fa-regular fa-file-lines"></i> New  client has been added .'
        })
    })
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@require_http_methods(['DELETE','GET'])
def deleteClient(request,id):
    data=Customer.objects.get(pk=id)
    if request.method=="DELETE":
        data.delete()
        return HttpResponse(status=204,
                                headers={
                                    'HX-Trigger': json.dumps({
                                    "crmChange": None,
                                    "close":"close",
                                    "showMessage": f"{data.company} Has been deleted ."
            })
        })
    return render (request,"crm/deletemodal.html",{"customer":data})

@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@require_http_methods(['POST'])
def search_industry(request):
    search_text = request.POST.get('industry')
    iddata=Industry.objects.get(name__icontains=search_text)
    results=Customer.objects.all().filter(industry=iddata.id)
    context={
        'customers':results,

        }
    return render(request,'crm/listing.html',context)
@login_required
@require_http_methods(['POST'])
def search_status(request):
    search_text = request.POST.get('status')
    print(search_text)
    iddata=Status.objects.get(type__icontains=search_text)
    results=Customer.objects.all().filter(status=iddata.id)
    context={
        'customers':results,

        }
    return render(request,'crm/listing.html',context)
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
@require_http_methods(['POST'])
def search_client(request):
    search_text = request.POST.get('search')
    results= Customer.objects.filter(company__icontains=search_text)
    context={
        'customers':results,

        }
    return render(request,'crm/listing.html',context)

@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def Customerlistview(request):
    customer=Customer.objects.all()
    industry=Industry.objects.all()
    statuses=Status.objects.all()
    form=CustomerForm
    context={
        'customers':customer,
        'industrys':industry,
        'statuses':statuses,
        'form':form,
        'title':'Customers List',
        }
    
    return render (request,'crm/list.html',context)
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def view_edit_customer(request,id):
    customer=get_object_or_404(Customer,pk=id)
    form=CustomerForm(instance=customer)
    customers=Customer.objects.all()
    contacts=customer.contact_set.all()
    contactform=Addcontanct
    context={"customer":customer,"edit_form":form,"customers":customers,"contacts":contacts,"contactform":contactform,}
    if request.method == 'GET':
        return render(request,'crm/show_modal.html',context)
    elif request.method == "PUT":
        data=QueryDict(request.body).dict()
        form=CustomerForm(data,instance=customer)
        if form.is_valid:
            form.save()
            return HttpResponse(status=204,
                            headers={
                                'HX-Trigger': json.dumps({
                                "crmChange": None,
                                "showMessage": f"{customer.company} details has been edited successfully.",
                                "type":"bg-success"
                                
                                })})
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def emails(request,id):
    customer=get_object_or_404(Customer,pk=id)
    form=Customer_Email_Form(request.POST)
    customers=Customer.objects.all()
    context={"customer":customer,"email_form":form,"customers":customers}
    if request.method == 'GET':
        return render(request,'crm/send_email.html',context)
    if request.method=='POST' and "simple-mail" in request.POST:
        if customer.email:
            if form.is_valid():
                form.save()
            subject=request.POST.get("subject")
            message=request.POST.get("message")
            company=request.POST.get("company")
            sender=request.POST.get("sender")
            try:
                file=request.FILES["file_upload"]
                customer_email=get_object_or_404(Customer,pk=company).email
                user_email=get_object_or_404(User,pk=sender).email
                email = EmailMultiAlternatives(
                    subject,
                    message,
                    user_email,
                    [customer_email],
                    )
                email.attach(file.name,file.read(),file.content_type)

                    

                email.send()
                print(subject,message,customer_email,user_email)
                return HttpResponse(status=204,
                                    headers={
                                        'HX-Trigger': json.dumps({
                                        "emailChange": None,
                                        "close": "close",
                                        "showMessage": f"Email Sent To {customer.company} .",
                                        "type":"bg-success"
                })
            })
            except:
                customer_email=get_object_or_404(Customer,pk=company).email
                user_email=get_object_or_404(User,pk=sender).email
                email = EmailMultiAlternatives(
                    subject,
                    message,
                    user_email,
                    [customer_email],
                    )
                email.send()
                print(subject,message,customer_email,user_email)
                return HttpResponse(status=204,
                                    headers={
                                        'HX-Trigger': json.dumps({
                                        "emailChange": None,
                                        "close": "close",
                                        "showMessage": f"Email Sent To {customer.company} .",
                                        "type":"bg-success"
                })
            })
        else:
            return HttpResponse(status=204,
                                    headers={
                                        'HX-Trigger': json.dumps({
                                        "emailChange": None,
                                        "close": "close",
                                        "showMessage": f"{customer.company} Dont have email address add email then try again .",
                                        "type":"bg-danger",
                })
            })

    elif request.method=='POST' and "template" in request.POST:
        
        company=request.POST.get('company')
        email=request.POST.get('email')
        content=request.POST.get('emailtype')
        content_sent=""
        Customer_Email.objects.create(subject="template",message="Template Content",sender=request.user,company=Customer.objects.get(company__icontains=company))
        link="https://www.facebook.com/Almazadiii"
        insta="https://www.instagram.com/almazadi.official/"
        template= get_template('email.txt')
        context={
            'company':company,
            'downloadlink':link,
            'facebooklink':link,
            'instgramlink':insta,
            'twitterlink':link,
        }
        message=template.render(context)
        email = EmailMultiAlternatives(
            "Al-Mazadi",message,
            "mada",
            ['ah.abolaban@gmail.com',email]
            )
        email.content_subtype='html'
        email.send()
        
        return HttpResponse(status=204,
                            headers={
                                'HX-Trigger': json.dumps({
                                "emailChange": None,
                                "showMessage": f"Email Sent To {customer.company} .",
                                "close": "close",
                                "type":"bg-success"
        })
    })
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def veiw_client(request,id):
    customer=get_object_or_404(Customer,pk=id)
    context={"customer":customer}
    return render(request,'crm/customer_modal_info.html',context)
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def customerlist_json(request):
    customers=Customer.objects.all()
    data=[customer.get_data() for customer in customers]
    response={'data': data}
    return JsonResponse(response)

#def email_templates(request):
     #return render(request,"crm/email_templates.html") 


@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)   
def toast(request):
    return render(request,"crm/toast.html")
    
    

    

@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer=form.save()
            return HttpResponse(status=204,
            headers={
                    'HX-Trigger': json.dumps({
                        "crmChange": None,
                        "showMessage": f"{customer.company} added.",
                        "close": "close",
                        "type":"bg-success"
                    })
                })
    else:
        form = CustomerForm()
    return render(request, 'crm/add.html', {
        'form': form,
    })
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)    
def view_add_contact(request,id):
    if request.method == "GET":
        customer=get_object_or_404(Customer,pk=id)
        contacts=customer.contact_set.all()
        return render (request,"crm/contacts.html",{"contacts":contacts})
    if request.method == "POST":
        form=Addcontanct(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204,
                    headers={
                            'HX-Trigger': json.dumps({
                                "contactChange": None,
                                "showMessage": f"contact added successfully.",
                                "type":"bg-success"
                            })
                        })
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)                        
def delete_contact(request,id):
    contact=get_object_or_404(Contact,pk=id)
    contact.delete()
    return HttpResponse(status=204,
                    headers={
                            'HX-Trigger': json.dumps({
                                "contactChange": None,
                                "showMessage": f"contact deleted successfully.",
                                "type":"bg-success"
                            })
                        })
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def client_profile(request,id):
    customer=get_object_or_404(Customer,pk=id)
    contact=customer.contact_set.all()
    note=customer.contact_set.all()
    email=customer.contact_set.all()
    customerform=CustomerForm(instance=customer)
    context={
        "customer":customer,
        "contacts":contact,
        "notes":note,
        "emails":email,
        "title":"Client Profile",
        "edit_form":customerform,
    }
    return render(request,"crm/client_profile.html",context)
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def client_emails(request,id):
    customer=get_object_or_404(Customer,pk=id)
    email=customer.customer_email_set.all()
    context={
        "customer":customer,
        "emails":email,

    }
    return render(request,"crm/client_emails.html",context)
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def client_notes(request,id):
    customer=get_object_or_404(Customer,pk=id)
    note=customer.note_set.all()
    context={
        "customer":customer,
        "notes":note,
    }
    return render(request,"crm/client_notes.html",context)
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def client_products(request,id):
    customer=get_object_or_404(Customer,pk=id)
    product=customer.customer_product_set.all()
    context={
        "customer":customer,
        "products":product,
    }
    return render(request,"crm/client_products.html",context)
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def client_invoice(request,id):
    customer=get_object_or_404(Customer,pk=id)
    invoices=customer.invoice_set.all()
    context={
        "customer":customer,
        "invoices":invoices,
    }
    return render(request,"crm/client_invoices.html",context)
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def profile_data(request,id):
    customer=get_object_or_404(Customer,pk=id)
    context={
        "customer":customer,
    }
    return render(request,"crm/profile_data.html",context)
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def show_note(request,id):
    note=get_object_or_404(Note,pk=id)
    context={
        "note":note,
    }
    return render(request,"crm/show_note.html",context)
@login_required
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def add_note(request,id):
    if request.method=="POST":
        form=Addnote(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204,
                    headers={
                            'HX-Trigger': json.dumps({
                                "noteChange": None,
                                "showMessage": f"Note as been added successfully.",
                                "close": "close",
                                "type":"bg-info"
                            })
                        })
    else:
        form=Addnote
        customer=get_object_or_404(Customer,pk=id)
        context={
            "customer":customer,
            "form":form,
        }
        
        return render(request,"crm/add_note.html",context)
def show_email(request,id):
    email=get_object_or_404(Customer_Email,id=id)

    context={

        'email':email
        }

    return render(request,"crm/show_email.html",context)
def send_whatsapp(request,id):
    customer=get_object_or_404(Customer,id=id)
    if request.method=="POST":
        number=request.POST.get("number")
        message=request.POST.get("message")
        type=request.POST.get("emailtype")
        try:
            url=request.POST.get("url")
        except:
            url=None
        if type == "text":
            response=send_whatsapp_message(number,str(message))
            if response["sent"]=="true":
                return HttpResponse(status=204,
                        headers={
                                'HX-Trigger': json.dumps({
                                    "noteChange": None,
                                    "showMessage": f"Message sent to {customer.company}",
                                    "close": "close",
                                    "type":"bg-success"
                                })
                            })
            else:
                return HttpResponse(status=204,
                        headers={
                                'HX-Trigger': json.dumps({
                                    "noteChange": None,
                                    "showMessage": f"Message Error!",
                                    "type":"bg-danger"
                                })
                            })
        elif type == "pdf":
            response=send_whatsapp_pdf(number,str(message),url)
            if response["sent"]=="true":
                return HttpResponse(status=204,
                        headers={
                                'HX-Trigger': json.dumps({
                                    "noteChange": None,
                                    "showMessage": f"Message sent to {customer.company}",
                                    "close": "close",
                                    "type":"bg-success"
                                })
                            })
            else:
                return HttpResponse(status=204,
                        headers={
                                'HX-Trigger': json.dumps({
                                    "noteChange": None,
                                    "showMessage": f"Message Error!",
                                    "type":"bg-danger"
                                })
                            })
        elif type == "image":
            response=send_whatsapp_img(number,str(message),url)
            if response["sent"]=="true":
                return HttpResponse(status=204,
                        headers={
                                'HX-Trigger': json.dumps({
                                    "noteChange": None,
                                    "showMessage": f"Message sent to {customer.company}",
                                    "close": "close",
                                    "type":"bg-success"
                                })
                            })
            else:
                return HttpResponse(status=204,
                        headers={
                                'HX-Trigger': json.dumps({
                                    "noteChange": None,
                                    "showMessage": f"Message Error!",
                                    "type":"bg-danger"
                                })
                            })
        elif type == "video":
            response=send_whatsapp_video(number,str(message),url)
            if response["sent"]=="true":
                return HttpResponse(status=204,
                        headers={
                                'HX-Trigger': json.dumps({
                                    "noteChange": None,
                                    "showMessage": f"Message sent to {customer.company}",
                                    "close": "close",
                                    "type":"bg-success"
                                })
                            })
            else:
                return HttpResponse(status=204,
                        headers={
                                'HX-Trigger': json.dumps({
                                    "noteChange": None,
                                    "showMessage": f"Message Error!",
                                    "type":"bg-danger"
                                })
                            })
        else:
            return HttpResponse(status=204,
                        headers={
                                'HX-Trigger': json.dumps({
                                    "noteChange": None,
                                    "showMessage": f"Message Error!",
                                    "type":"bg-danger"
                                })
                            })


    context={"customer":customer}
    return render(request,"crm/send_whatsapp.html",context)