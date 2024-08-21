# Generated by Django 5.0.1 on 2024-08-21 08:36

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_alter_sustainability_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]