# Generated by Django 4.2.6 on 2023-11-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_album_a_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='p_url',
        ),
        migrations.AddField(
            model_name='photo',
            name='p_images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]