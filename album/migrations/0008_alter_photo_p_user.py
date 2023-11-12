# Generated by Django 4.2.6 on 2023-11-12 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('album', '0007_rename_user_photo_p_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='p_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]