# Generated by Django 3.0.2 on 2020-12-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20201217_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roominstance',
            name='status',
            field=models.CharField(choices=[('O', 'Occupied'), ('U', 'Unoccupied'), ('M', 'Maintanence')], default='U', max_length=1),
        ),
    ]