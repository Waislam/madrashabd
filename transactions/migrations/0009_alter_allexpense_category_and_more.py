# Generated by Django 4.0.6 on 2022-09-05 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_expensecategory_expensesubcategory_allexpense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allexpense',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expense_categories', to='transactions.expensecategory'),
        ),
        migrations.AlterField(
            model_name='allexpense',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expense_sub_categories', to='transactions.expensesubcategory'),
        ),
    ]
