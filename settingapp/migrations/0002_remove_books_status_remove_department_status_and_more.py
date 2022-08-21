# Generated by Django 4.0.6 on 2022-08-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='status',
        ),
        migrations.RemoveField(
            model_name='department',
            name='status',
        ),
        migrations.RemoveField(
            model_name='designation',
            name='status',
        ),
        migrations.RemoveField(
            model_name='examrules',
            name='status',
        ),
        migrations.RemoveField(
            model_name='fees',
            name='status',
        ),
        migrations.RemoveField(
            model_name='madrashaclasses',
            name='status',
        ),
        migrations.RemoveField(
            model_name='madrashagroup',
            name='status',
        ),
        migrations.RemoveField(
            model_name='session',
            name='status',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='status',
        ),
        migrations.AddField(
            model_name='books',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='department',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='designation',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='examrules',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fees',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='madrashaclasses',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='madrashagroup',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='session',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='shift',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
