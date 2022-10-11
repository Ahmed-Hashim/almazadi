from django.db import models
from crm.models import Customer
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.name)

class Customer_products(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
