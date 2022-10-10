import json


file=open('/home/mada/python-projects/PC-Python/mazadi/src/crm/stores.json','r',encoding='UTF-8')

data = json.load(file)

for i in range(0,900):
    try:
        datsa=data['customers'][i]
        name=datsa['name']
        phones=datsa['phones'].split(',')
        Customer.objects.create(company=name)
        for phone in phones:
            PhoneNumbers.objects.create(
                company=name,
                phone_number=phone.replace("'",""))
    except:
        print('something wronge')



    file=open('/home/mada/python-projects/PC-Python/mazadi/src/crm/stores.json','r',encoding='UTF-8')

    data = json.load(file)

    for i in range(0,853):
        try:
            datsa=data['customers'][i]
            nassme=datsa['name']
            phones=datsa['phones'].split(',')
            #Customer.objects.create(company=name)
            for phone in phones:
                company=Customer.objects.filter(company=nassme).values('id')[0]['id']
                print(company)
                PhoneNumbers.objects.get_or_create(
                    company_id=company,
                    phone_number=phone.replace("'",""))
        except:
            pass
