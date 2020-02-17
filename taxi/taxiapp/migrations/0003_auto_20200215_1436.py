# Generated by Django 3.0.3 on 2020-02-15 12:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxiapp', '0002_auto_20200214_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='car_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='Passenger', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default=None, max_length=12, validators=[django.core.validators.RegexValidator('^\\d+$', 'Only numeric characters are allowed.'), django.core.validators.MaxLengthValidator]),
        ),
        migrations.AddField(
            model_name='order',
            name='surname',
            field=models.CharField(default='Passenger', max_length=50),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]