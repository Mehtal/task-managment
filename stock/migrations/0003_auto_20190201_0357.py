# Generated by Django 2.1.5 on 2019-02-01 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20190131_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supply',
            old_name='price',
            new_name='unit_price',
        ),
    ]