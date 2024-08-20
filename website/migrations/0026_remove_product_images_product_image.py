# Generated by Django 5.0.1 on 2024-08-19 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_alter_product_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]