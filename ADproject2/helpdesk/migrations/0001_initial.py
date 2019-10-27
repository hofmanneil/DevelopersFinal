# Generated by Django 2.2.6 on 2019-10-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine', models.CharField(default=None, max_length=200)),
                ('machine_serial', models.CharField(default=None, max_length=200)),
                ('monitor_serial', models.CharField(default=None, max_length=200)),
                ('monitor_type', models.CharField(default=None, max_length=200)),
                ('special_request', models.CharField(default=None, max_length=200)),
                ('special', models.CharField(default=None, max_length=200)),
                ('keyboard', models.CharField(default=None, max_length=200)),
                ('mouse', models.CharField(default=None, max_length=200)),
                ('headset', models.CharField(default=None, max_length=200)),
                ('bag', models.CharField(default=None, max_length=200)),
                ('fulfilled_date', models.DateTimeField(auto_now_add=True)),
                ('thumb', models.ImageField(blank=True, upload_to='', verbose_name='default.png')),
            ],
        ),
    ]