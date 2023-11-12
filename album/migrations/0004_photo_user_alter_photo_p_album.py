# Generated by Django 4.2.6 on 2023-11-12 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('album', '0003_remove_photo_p_url_photo_p_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='p_album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='album.album'),
        ),
    ]
