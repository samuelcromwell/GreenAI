# Generated by Django 5.0.1 on 2024-08-12 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_product_detailed_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='brief_description',
        ),
    ]
