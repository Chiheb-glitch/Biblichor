# Generated by Django 3.1 on 2022-07-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220721_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='codepostal',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='etat',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='goodreads',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='userprofile/169660610_913026526206945_1802319886465244479_n.jpg', upload_to='userprofile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='vilee',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='whattpad',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]