# Generated by Django 5.1.2 on 2024-10-23 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrName', models.TextField(max_length=30)),
                ('pswd', models.TextField(max_length=30)),
            ],
        ),
    ]