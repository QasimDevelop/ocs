# Generated by Django 5.1.2 on 2024-10-23 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_user_id_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
