# Generated by Django 3.1 on 2022-08-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20220807_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address_line_1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='codepostal',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='etat',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='vilee',
            field=models.CharField(max_length=20),
        ),
    ]
