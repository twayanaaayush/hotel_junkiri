# Generated by Django 3.0.2 on 2020-12-17 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0013_auto_20201217_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=50, verbose_name='Name')),
                ('u_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('u_contact', models.IntegerField(verbose_name='Contact')),
                ('u_address', models.CharField(max_length=50, verbose_name='Address')),
                ('u_room', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.RoomInstance')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
