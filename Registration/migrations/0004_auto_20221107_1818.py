# Generated by Django 3.1.13 on 2022-11-07 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_auto_20221107_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='id',
            new_name='ids',
        ),
    ]
