# Generated by Django 3.1 on 2022-08-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_reviewrationg_username_add_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_verif',
            field=models.BooleanField(default=False),
        ),
    ]