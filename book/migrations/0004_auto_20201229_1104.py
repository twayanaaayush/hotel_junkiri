# Generated by Django 3.0.2 on 2020-12-29 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20201217_1108'),
        ('book', '0003_auto_20201229_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.Room'),
        ),
    ]
