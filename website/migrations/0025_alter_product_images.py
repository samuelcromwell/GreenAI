# Generated by Django 5.0.1 on 2024-08-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_remove_product_image_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.JSONField(default=list),
        ),
    ]