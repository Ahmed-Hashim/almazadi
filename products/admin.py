from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Customer_product)
admin.site.register(Invoice)