# Generated by Django 4.2.6 on 2023-11-02 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_comment', '0006_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
