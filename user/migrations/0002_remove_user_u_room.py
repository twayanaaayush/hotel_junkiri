# Generated by Django 3.0.2 on 2020-12-29 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='u_room',
        ),
    ]
