# Generated by Django 3.1 on 2022-07-08 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_access_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='access_level',
        ),
    ]