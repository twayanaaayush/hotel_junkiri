# Generated by Django 3.0.2 on 2021-03-09 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20201229_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='user',
            new_name='usr',
        ),
    ]
