# Generated by Django 3.1 on 2022-07-27 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20220727_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default='1'),
        ),
    ]