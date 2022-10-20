from decimal import Decimal
from django.db import models
from crm.models import Customer, Note
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse
from datetime import timedelta, date

# Create your models here.
class Product(models.Model):
    CURRENCY=[
    ("DZD","DZD")
    ]
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    time_period=models.IntegerField(null=True,blank=True,)
    price=models.DecimalField(null=True,blank=True,max_digits=100, decimal_places=2,)
    currency=models.CharField(choices=CURRENCY,default="DZD",max_length=100)
    uniqueId =models.CharField(null=True,blank=True,max_length=100)
    slug=models.SlugField(max_length=500,unique=True,null=True,blank=True)
    date_created=models.DateTimeField(null=True,blank=True)
    date_updated=models.DateTimeField(null=True,blank=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.name,self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.name, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.name, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Product, self).save(*args, **kwargs)


class Invoice(models.Model):
    STATUS=[
    ('CURRENT', 'CURRENT'),
    ('EMAIL_SENT', 'EMAIL_SENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
]
    TERMS = [
    ('14 days', '14 days'),
    ('30 days', '30 days'),
    ('60 days', '60 days'),
    ]
    #RELATED fields
    customerid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    employeeid=models.ForeignKey(User,on_delete=models.CASCADE)
    #Invoice Data fields
    note=models.TextField(max_length=1000)
    status=models.CharField(max_length=100,choices=STATUS,default='CURRENT')
    products=models.ManyToManyField(Product,related_name='products')
    paymentTerms = models.CharField(choices=TERMS, default='14 days', max_length=100)
    discount_presentage=models.IntegerField(blank=True, null=True)
    #cost_tax
    #cost

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.customerid, self.uniqueId)


    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.customerid, self.uniqueId))          
        

        self.slug = slugify('{} {}'.format(self.customerid, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Invoice, self).save(*args, **kwargs)


class Customer_product(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customerid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    invoiceid=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    start_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True,blank=True)

    def save(self, *args, **kwargs):
        product=Product.objects.get(pk=self.product.id)
        self.start_date = timezone.localtime(timezone.now())
        if product.time_period:
            if self.end_date is None:
                self.end_date = self.start_date+ timedelta(days=product.time_period)
            super(Customer_product, self).save(*args, **kwargs)
        else:
            super(Customer_product, self).save(*args, **kwargs)