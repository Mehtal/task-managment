# Generated by Django 2.1.5 on 2019-01-28 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagment', '0002_remove_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
