# Generated by Django 3.0.2 on 2020-12-14 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_service_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image_url',
            field=models.ImageField(default='/service_images/default.png', upload_to='service_images'),
        ),
    ]
