# Generated by Django 3.2.2 on 2021-10-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NanoWareControl', '0021_auto_20211020_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moisture_checker',
            name='date',
            field=models.CharField(default='20 Oct', max_length=16),
        ),
    ]
