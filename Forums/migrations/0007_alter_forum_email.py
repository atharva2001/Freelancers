# Generated by Django 4.2.1 on 2023-05-10 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forums', '0006_forum_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
