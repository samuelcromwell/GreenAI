# Generated by Django 5.0.1 on 2024-08-05 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_blog_meta_remove_blog_thumbnail_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
    ]
