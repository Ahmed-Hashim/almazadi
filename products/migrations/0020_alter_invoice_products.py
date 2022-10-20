# Generated by Django 4.1 on 2022-10-18 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_customer_product_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='products', to='products.product'),
        ),
    ]