# Generated by Django 3.1 on 2022-08-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20220806_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(error_messages={'invalid': 'you custom error message'}, max_length=50, unique=True),
        ),
    ]