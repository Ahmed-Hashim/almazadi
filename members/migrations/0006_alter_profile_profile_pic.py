# Generated by Django 4.1 on 2022-08-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_remove_profile_profile_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/images/profile/default-profile.jpg', null=True, upload_to='images/profile/'),
        ),
    ]
