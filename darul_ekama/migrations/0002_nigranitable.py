# Generated by Django 4.1.2 on 2022-11-16 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('settingapp', '0011_room_floor'),
        ('teachers', '0002_experience_alter_teacher_skill_teacher_experience'),
        ('darul_ekama', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NigraniTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.CharField(max_length=3)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='building_nigrans', to='settingapp.building')),
                ('class_nigran', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_nigrans', to='settingapp.madrashaclasses')),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='madrasha_darul_ekam_nigrani', to='accounts.madrasha')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room_nigran', to='settingapp.room')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_nigrani', to='teachers.teacher')),
            ],
        ),
    ]
