# Generated by Django 4.1 on 2022-10-22 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0022_alter_customer_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='status',
            new_name='Situation',
        ),
    ]
