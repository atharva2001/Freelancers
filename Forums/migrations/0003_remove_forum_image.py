# Generated by Django 3.1.13 on 2023-05-05 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forums', '0002_auto_20230505_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='image',
        ),
    ]
