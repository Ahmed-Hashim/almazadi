from django.contrib import admin

from .models import *
# Register your models here.
class CustomerEmailAdmin(admin.ModelAdmin):
    list_display=('subject',
            'sender',
            'company',
            'file_upload',
            'message',)
    search_fields=('company',)
    list_per_page=25

admin.site.register(Note)
admin.site.register(Customer_Email)
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Industry)
admin.site.register(Status)