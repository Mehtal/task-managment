# Generated by Django 2.1.5 on 2019-03-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagment', '0008_auto_20190227_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='last_modefied',
            field=models.DateTimeField(auto_now=True),
        ),
    ]