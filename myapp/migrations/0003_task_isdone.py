# Generated by Django 5.0.7 on 2024-08-18 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]
