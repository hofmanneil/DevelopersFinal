# Generated by Django 2.2.6 on 2019-10-17 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0003_inventory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='bag',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='headset',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='keyboard',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='mouse',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='special_request',
            field=models.BooleanField(default=False),
        ),
    ]
