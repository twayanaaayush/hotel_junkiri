# Generated by Django 3.0.2 on 2021-03-09 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_roominstance_u_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roominstance',
            old_name='u_room',
            new_name='user',
        ),
    ]
