# Generated by Django 5.0.1 on 2024-08-26 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0045_alter_feedback_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='sent_at',
            new_name='received_at',
        ),
    ]
