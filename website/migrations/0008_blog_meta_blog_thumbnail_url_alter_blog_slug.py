# Generated by Django 5.0.1 on 2024-08-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_blog_meta_remove_blog_thumbnail_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='meta',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbnail_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
