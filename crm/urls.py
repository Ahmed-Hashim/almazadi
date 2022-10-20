from django.urls import path
from . import views

from .api import crmapi

urlpatterns = [
    ###################################################################
    ########################### List URLS #############################
    ###################################################################
    path('customerlist', views.customerlist,name='customerlist'),
    path('list', views.Customerlistview,name='crm_list'),    
    path('listing', views.customerlist,name='listing'),
    ###################################################################
    ########################### CRUD URLS #############################
    ###################################################################
    path('add_client', views.AddClient,name='add_client'),
    path('delete_client/p=<int:id>', views.deleteClient,name='delete_client'),
    path('view_edit_customer/p=<int:id>', views.view_edit_customer,name='view_edit_customer'),
    path('veiw_client/p=<int:id>', views.veiw_client,name='veiw_client'),
    path('add_customer/', views.add_customer,name='add_customer'),    
    path('view_add_contact/p=<int:id>', views.view_add_contact,name='view_add_contact'),    
    path('delete_contact/p=<int:id>', views.delete_contact,name='delete_contact'),    
    ###################################################################
    ########################### Email URLS ############################
    ###################################################################
    path('emails/p=<int:id>', views.emails,name='emails'),
    ###################################################################
    ########################### Random URLS ###########################
    ###################################################################
    path('json/', views.customerlist_json,name='customerlist_json'),
    path('toast/', views.toast,name='toast'),
    ###################################################################
    ###################### Client Profile URLS ########################
    ###################################################################
    path('client_profile/p=<int:id>', views.client_profile,name='client_profile'),
    path('client_emails/p=<int:id>', views.client_emails,name='client_emails'),
    path('client_notes/p=<int:id>', views.client_notes,name='client_notes'),
    path('profile_data/p=<int:id>', views.profile_data,name='profile_data'),
    path('client_products/p=<int:id>', views.client_products,name='client_products'),
    path('client_invoice/p=<int:id>', views.client_invoice,name='client_invoice'),
    path('show_note/p=<int:id>', views.show_note,name='show_note'),
    path('add_note/p=<int:id>', views.add_note,name='add_note'),

   
    
    #path('list', views.Customerlist,name='crm_list'),
    #path('list', views.CustomerList.as_view(),name='crm_list'),
    #path('edit_customer/p=<int:id>', views.edit_customer,name='edit_customer'),
    #path('search_client/', views.search_client,name='search_client'),
    #path('search_industry/', views.search_industry,name='search_industry'),
    #path('search_status/', views.search_status,name='search_status'),
    #path('email_templates', views.email_templates,name='email_templates'),
    #path('send_email', views.send_email,name='send_email'),


    path('api/',crmapi.urls)

]