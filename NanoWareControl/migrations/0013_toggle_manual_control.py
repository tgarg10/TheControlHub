# Generated by Django 3.2.2 on 2021-10-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NanoWareControl', '0012_auto_20211012_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toggle_Manual_Control',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
