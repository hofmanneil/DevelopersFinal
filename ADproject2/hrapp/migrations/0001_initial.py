# Generated by Django 2.2.6 on 2019-10-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teudat_zehut', models.CharField(default=None, max_length=20)),
                ('firstname', models.CharField(default=None, max_length=20)),
                ('lastname', models.CharField(default=None, max_length=20)),
                ('username', models.CharField(default=None, max_length=20)),
                ('email_address', models.CharField(default=None, max_length=20)),
                ('phone_number', models.CharField(default=None, max_length=20)),
                ('department', models.CharField(default=None, max_length=20)),
                ('office', models.CharField(default=None, max_length=20)),
                ('fulfilled_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
