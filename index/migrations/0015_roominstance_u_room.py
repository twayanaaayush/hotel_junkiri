# Generated by Django 3.0.2 on 2021-03-09 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_user_u_room'),
        ('index', '0014_auto_20201229_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='roominstance',
            name='u_room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.User'),
        ),
    ]
