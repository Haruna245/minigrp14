# Generated by Django 4.0.3 on 2022-05-22 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='apartment_describ',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='houses',
            name='apartment_img1',
            field=models.ImageField(blank=True, null=True, upload_to='images/apartments/'),
        ),
        migrations.AddField(
            model_name='houses',
            name='apartment_img2',
            field=models.ImageField(blank=True, null=True, upload_to='images/apartments/'),
        ),
        migrations.AddField(
            model_name='houses',
            name='apartment_img3',
            field=models.ImageField(blank=True, null=True, upload_to='images/apartments/'),
        ),
        migrations.AddField(
            model_name='houses',
            name='apartment_img4',
            field=models.ImageField(blank=True, null=True, upload_to='images/apartments/'),
        ),
        migrations.AddField(
            model_name='houses',
            name='apartment_location',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='houses',
            name='apartment_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='houses',
            name='book',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='houses',
            name='rent_period',
            field=models.TextField(null=True),
        ),
    ]
