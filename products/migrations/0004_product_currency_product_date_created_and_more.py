# Generated by Django 4.1 on 2022-10-14 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0021_alter_note_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_customer_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('DA', 'DZD')], default='DA', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='date_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='uniqueID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateTimeField()),
                ('note', models.TextField(max_length=1000)),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('not paid', 'Not Paid')], max_length=100)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.customer')),
                ('employeeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(to='products.product')),
            ],
        ),
    ]