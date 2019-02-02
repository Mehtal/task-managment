# Generated by Django 2.1.5 on 2019-01-29 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagment', '0003_task_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='area',
        ),
        migrations.AddField(
            model_name='tool',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tools', to='taskmanagment.Project'),
            preserve_default=False,
        ),
    ]
