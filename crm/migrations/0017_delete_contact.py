# Generated by Django 4.1 on 2022-10-04 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0016_customer_land_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
