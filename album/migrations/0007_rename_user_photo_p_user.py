# Generated by Django 4.2.6 on 2023-11-12 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0006_photo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='user',
            new_name='p_user',
        ),
    ]