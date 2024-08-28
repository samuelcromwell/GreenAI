# Generated by Django 5.0.1 on 2024-08-28 16:56

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0047_knowledge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whitepaper',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
        ),
    ]