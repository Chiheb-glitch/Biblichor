# Generated by Django 3.1 on 2022-07-21 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='state',
        ),
    ]
