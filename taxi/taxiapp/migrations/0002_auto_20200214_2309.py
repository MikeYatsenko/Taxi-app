# Generated by Django 3.0.3 on 2020-02-14 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cars',
            new_name='Car',
        ),
        migrations.RenameModel(
            old_name='Customers',
            new_name='Customer',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
