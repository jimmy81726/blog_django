# Generated by Django 4.2.6 on 2023-11-03 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_comment', '0011_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date_added',
            new_name='comment_added',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment_content',
        ),
    ]