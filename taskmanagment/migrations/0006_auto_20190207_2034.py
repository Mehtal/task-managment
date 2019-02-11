# Generated by Django 2.1.5 on 2019-02-07 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagment', '0005_task_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tool',
            old_name='price',
            new_name='unit_price',
        ),
        migrations.AddField(
            model_name='tool',
            name='task',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tools', to='taskmanagment.Task'),
            preserve_default=False,
        ),
    ]