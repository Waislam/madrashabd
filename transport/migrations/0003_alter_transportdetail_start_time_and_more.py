# Generated by Django 4.1.2 on 2022-11-02 20:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0002_alter_transportdetail_start_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportdetail',
            name='start_time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='vehicleinfo',
            name='time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
