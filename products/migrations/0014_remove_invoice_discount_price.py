# Generated by Django 4.1 on 2022-10-17 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_invoice_discount_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='discount_price',
        ),
    ]
