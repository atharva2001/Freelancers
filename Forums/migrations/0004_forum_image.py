# Generated by Django 3.1.13 on 2023-05-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forums', '0003_remove_forum_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
