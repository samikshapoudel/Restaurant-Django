# Generated by Django 2.2.3 on 2019-07-22 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='custom_user',
            name='cv',
        ),
        migrations.RemoveField(
            model_name='custom_user',
            name='photo',
        ),
    ]
