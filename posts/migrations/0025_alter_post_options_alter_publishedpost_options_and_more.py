# Generated by Django 4.1 on 2022-09-07 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_publishedpost_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='publishedpost',
            options={'ordering': ('-published_date',)},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ('date_to_publish',)},
        ),
    ]
