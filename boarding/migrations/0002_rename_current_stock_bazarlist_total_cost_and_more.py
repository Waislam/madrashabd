# Generated by Django 4.0.6 on 2022-10-01 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('boarding', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bazarlist',
            old_name='current_stock',
            new_name='total_cost',
        ),
        migrations.RemoveField(
            model_name='bazarlist',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='bazarlist',
            name='bazar_item_name',
        ),
        migrations.RemoveField(
            model_name='bazarlist',
            name='consumption',
        ),
        migrations.RemoveField(
            model_name='bazarlist',
            name='quantity',
        ),
        migrations.CreateModel(
            name='BazarItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bazar_item_name', models.CharField(max_length=250)),
                ('quantity', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250)),
                ('consumption', models.CharField(max_length=250)),
                ('total_stock', models.CharField(blank=True, max_length=250, null=True)),
                ('madrasha', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bazarItem_madrasha', to='accounts.madrasha')),
            ],
        ),
        migrations.AddField(
            model_name='bazarlist',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bazarList_item', to='boarding.bazaritem'),
        ),
    ]
