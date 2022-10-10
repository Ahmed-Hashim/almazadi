from ninja import NinjaAPI,ModelSchema
from .models import Customer
from typing import List

crmapi = NinjaAPI()

class CustomerSchema(ModelSchema):
    class Config:
        model = Customer
        model_fields = '__all__'


@crmapi.get('crmlist/',response=List[CustomerSchema])
def posts(request):
    return Customer.objects.all()
