# Generated by Django 4.1 on 2022-10-17 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_invoice_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
