# Generated by Django 5.0.1 on 2024-08-22 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0039_alter_opportunity_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='opportunity',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='opportunity_images/'),
        ),
    ]
