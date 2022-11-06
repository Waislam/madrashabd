# Generated by Django 4.1.2 on 2022-11-06 05:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settingapp', '0005_admitcardinfo'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_categories', to='transactions.incomecategory')),
            ],
        ),
        migrations.CreateModel(
            name='StudentIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_class_id', models.CharField(blank=True, max_length=30)),
                ('for_month', models.CharField(blank=True, choices=[('null', 'Null'), ('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=20, null=True)),
                ('for_months', models.CharField(blank=True, max_length=100, null=True)),
                ('paid_date', models.DateField(default=datetime.date.today)),
                ('receipt_number', models.CharField(blank=True, max_length=20)),
                ('student_id', models.CharField(blank=True, max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_cat', models.DateTimeField(auto_now=True)),
                ('voucher_name', models.CharField(blank=True, max_length=50)),
                ('amount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='amounts', to='settingapp.fees')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='transactions.incomecategory')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='st_incomes', to=settings.AUTH_USER_MODEL)),
                ('madrasha', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='students_incomes', to='accounts.madrasha')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sub_categories', to='transactions.incomesubcategory')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_st_icomes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OtherIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donar_name', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=15)),
                ('for_month', models.CharField(blank=True, choices=[('null', 'Null'), ('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=15, null=True)),
                ('for_months', models.CharField(blank=True, max_length=100, null=True)),
                ('paid_date', models.DateField(default=datetime.date.today)),
                ('receipt_book_number', models.CharField(blank=True, max_length=50, null=True)),
                ('receipt_page_number', models.CharField(blank=True, max_length=50, null=True)),
                ('receipt_number', models.CharField(blank=True, max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('voucher_name', models.CharField(blank=True, max_length=50)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='categories_others', to='transactions.incomecategory')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='other_incomes', to=settings.AUTH_USER_MODEL)),
                ('madrasha', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='other_incomes', to='accounts.madrasha')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sub_categories_others', to='transactions.incomesubcategory')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_other_incomes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expense_sub_cats', to='transactions.expensecategory')),
            ],
        ),
        migrations.CreateModel(
            name='AllExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_by', models.CharField(default='', max_length=250)),
                ('date', models.DateField(default=datetime.date.today)),
                ('for_month', models.CharField(blank=True, choices=[('null', 'Null'), ('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'), ('november', 'November'), ('december', 'December')], max_length=15, null=True)),
                ('for_months', models.CharField(blank=True, max_length=100, null=True)),
                ('receipt_number', models.CharField(blank=True, max_length=20)),
                ('description', models.CharField(default='', max_length=255)),
                ('approved_by', models.CharField(default='', max_length=255)),
                ('amount', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('voucher_name', models.CharField(blank=True, max_length=50)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expense_categories', to='transactions.expensecategory')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expenses', to=settings.AUTH_USER_MODEL)),
                ('madrasha', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='allexpenses', to='accounts.madrasha')),
                ('sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expense_sub_categories', to='transactions.expensesubcategory')),
                ('updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_expenses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
