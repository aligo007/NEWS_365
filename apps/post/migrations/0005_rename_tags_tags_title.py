# Generated by Django 4.0.5 on 2022-06-20 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_tags_post_tags_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='tags',
            new_name='title',
        ),
    ]
