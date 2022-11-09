# Generated by Django 4.1.2 on 2022-11-09 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='madrasha_departments', to='accounts.madrasha')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'madrasha')},
            },
        ),
        migrations.CreateModel(
            name='MadrashaClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_classes', to='settingapp.department')),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='madrasha_classes', to='accounts.madrasha')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'madrasha')},
            },
        ),
        migrations.CreateModel(
            name='ExamRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_input', models.TextField(max_length=2000)),
                ('is_active', models.BooleanField(default=True)),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='madrasha_exam_rules', to='accounts.madrasha')),
            ],
        ),
        migrations.CreateModel(
            name='AdmitCardInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talimat_name', models.CharField(max_length=255)),
                ('center_name', models.CharField(max_length=300)),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exam_admit_info', to='accounts.madrasha')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('shift_time', models.TimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_shifts', to='settingapp.department')),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='madrasha_shift', to='accounts.madrasha')),
                ('madrasha_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='class_shifts', to='settingapp.madrashaclasses')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'madrasha')},
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('actual_year', models.CharField(blank=True, max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='madrasha_sessions', to='accounts.madrasha')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'madrasha')},
            },
        ),
        migrations.CreateModel(
            name='MadrashaGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_madrasha_group', to='settingapp.department')),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='madrasha_groups', to='accounts.madrasha')),
                ('madrasha_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='class_madrasha_group', to='settingapp.madrashaclasses')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'madrasha')},
            },
        ),
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('amount', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_fees', to='settingapp.department')),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='madrasha_fees', to='accounts.madrasha')),
                ('madrasha_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='class_fees', to='settingapp.madrashaclasses')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'madrasha')},
            },
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_designations', to='settingapp.department')),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='madrasha_designations', to='accounts.madrasha')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'madrasha')},
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_books', to='settingapp.department')),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='madrasha_books', to='accounts.madrasha')),
                ('madrasha_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='class_books', to='settingapp.madrashaclasses')),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'madrasha')},
            },
        ),
    ]
