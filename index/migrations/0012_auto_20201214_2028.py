# Generated by Django 3.0.2 on 2020-12-14 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20201214_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='roominstance',
            name='id',
            field=models.AutoField(auto_created=True, default=101, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roominstance',
            name='room_number',
            field=models.IntegerField(),
        ),
    ]
