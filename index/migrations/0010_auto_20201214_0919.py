# Generated by Django 3.0.2 on 2020-12-14 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20201214_0837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='image_url',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='image_url',
            new_name='image',
        ),
    ]