# Generated by Django 4.1.2 on 2022-10-17 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0012_alter_studentincome_for_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentincome',
            name='for_month',
            field=models.CharField(blank=True, choices=[('null', 'Null'), ('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=20, null=True),
        ),
    ]
