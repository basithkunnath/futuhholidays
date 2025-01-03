# Generated by Django 5.1.4 on 2024-12-25 11:26

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='gallery_image',
            field=cloudinary.models.CloudinaryField(default='default_image_placeholder', max_length=255, verbose_name='image'),
        ),
    ]
