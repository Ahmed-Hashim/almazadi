# Generated by Django 4.1 on 2022-10-06 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0019_rename_postion_contact_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='writer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='notes',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
