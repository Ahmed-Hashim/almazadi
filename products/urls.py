from django.urls import path
from . import views


urlpatterns = [

    path('products', views.product_crud,name='product_crud'),
    path('products_list', views.products_list,name='products_list'),
    path('add_product', views.add_product,name='add_product'),
    path('delete_product/<int:id>', views.delete_product,name='delete_product'),
    path('edit_product/<int:id>', views.edit_product,name='edit_product'),
    path('invoice/<int:id>', views.invoice,name='invoice'),
    path('invoices', views.invoice_crud,name='invoice_crud'),
    path('invoices_list', views.invoices_list,name='invoices_list'),
    path('add_invoice', views.add_invoice,name='add_invoice'),
    path('show_invoice/<int:id>', views.show_invoice,name='show_invoice'),
    path('delete_invoice/<int:id>', views.delete_invoice,name='delete_invoice'),
    path('set_to_paid/<int:id>', views.set_to_paid,name='set_to_paid'),
    path('expiry_products', views.expiry_products,name='expiry_products'),



]