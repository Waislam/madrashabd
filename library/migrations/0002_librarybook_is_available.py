# Generated by Django 4.1.2 on 2022-10-19 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarybook',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]