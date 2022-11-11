# Generated by Django 4.1.2 on 2022-11-06 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('settingapp', '0005_admitcardinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='madrasha_buildings', to='accounts.madrasha')),
            ],
        ),
    ]
