# Generated by Django 4.0.6 on 2022-09-02 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_studentincome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incomecategory',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='incomesubcategory',
            old_name='category_name',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='incomesubcategory',
            old_name='sub_category_name',
            new_name='name',
        ),
    ]