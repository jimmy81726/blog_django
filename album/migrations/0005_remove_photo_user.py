# Generated by Django 4.2.6 on 2023-11-12 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_photo_user_alter_photo_p_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
    ]
