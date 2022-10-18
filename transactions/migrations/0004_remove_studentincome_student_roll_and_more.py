# Generated by Django 4.0.6 on 2022-09-03 09:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settingapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0003_rename_category_name_incomecategory_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentincome',
            name='student_roll',
        ),
        migrations.AddField(
            model_name='studentincome',
            name='amount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='amounts', to='settingapp.fees'),
        ),
        migrations.AddField(
            model_name='studentincome',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='studentincome',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='st_incomes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studentincome',
            name='for_month',
            field=models.CharField(choices=[('null', 'Null'), ('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], default='January', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='studentincome',
            name='for_months',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='studentincome',
            name='paid_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='studentincome',
            name='receipt_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='studentincome',
            name='student_class_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='studentincome',
            name='student_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='studentincome',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_st_icomes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studentincome',
            name='updated_cat',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
