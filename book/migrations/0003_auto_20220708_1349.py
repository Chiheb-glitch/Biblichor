# Generated by Django 3.1 on 2022-07-08 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='image',
            new_name='picture',
        ),
    ]
