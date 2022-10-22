from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_filter=["Situation",'industry']
    list_display=['company','first_name','last_name','lead_referral_source','industry','address','land_phone_number','email','website','status','last_contact_date',"_"]
    search_fields=['company','first_name','last_name','lead_referral_source','industry','land_phone_number','email','website','Situation']
    list_per_page=25

    def _(self,obj):
        if obj.Situation=="Active":
            return True
        elif obj.Situation=="Prospect":
            return None
        else:
            return False
    _.boolean = True
    def status(self,obj):
        if obj.Situation=="Active":
            color="#28a745"
        elif obj.Situation=="Prospect":
            color="#fea95e"
        else:
            color = "red"
        return format_html('<strong><p style="color:{}">{}</p></strong>'.format(color,obj.Situation))
    status.allow_tags = True

admin.site.register(Note)
admin.site.register(Customer_Email)
admin.site.register(Contact)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Industry)
admin.site.register(Status)