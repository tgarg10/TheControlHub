# Generated by Django 3.2.2 on 2021-10-11 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NanoWareControl', '0010_moisture_checker_water_irrigated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moisture_checker',
            name='date',
            field=models.CharField(default=datetime.date(2021, 10, 12), max_length=16),
        ),
        migrations.AlterField(
            model_name='water_irrigated',
            name='date',
            field=models.CharField(default=datetime.date(2021, 10, 12), max_length=16),
        ),
    ]