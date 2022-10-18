# Generated by Django 4.0.6 on 2022-09-03 16:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0006_studentincome_voucher_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donar_name', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=15)),
                ('for_month', models.CharField(choices=[('null', 'Null'), ('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], default='null', max_length=15)),
                ('for_months', models.CharField(blank=True, max_length=100, null=True)),
                ('paid_date', models.DateField(default=datetime.date.today)),
                ('receipt_book_number', models.CharField(blank=True, max_length=50, null=True)),
                ('receipt_page_number', models.CharField(blank=True, max_length=50, null=True)),
                ('receipt_number', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_cat', models.DateTimeField(auto_now=True)),
                ('voucher_name', models.CharField(blank=True, max_length=50)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories_others', to='transactions.incomecategory')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='other_incomes', to=settings.AUTH_USER_MODEL)),
                ('madrasha', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='other_incomes', to='accounts.madrasha')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sub_categories_others', to='transactions.incomesubcategory')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_other_incomes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]