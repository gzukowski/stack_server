# Generated by Django 4.2.11 on 2024-03-13 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task',
        ),
    ]
