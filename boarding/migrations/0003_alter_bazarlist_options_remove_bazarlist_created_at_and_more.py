# Generated by Django 4.0.6 on 2022-10-01 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boarding', '0002_rename_current_stock_bazarlist_total_cost_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bazarlist',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='bazarlist',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='bazarlist',
            name='updated_at',
        ),
    ]