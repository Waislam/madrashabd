# Generated by Django 4.1.2 on 2022-11-01 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_experience_alter_teacher_skill_teacher_experience'),
        ('students', '0003_mealinfo'),
        ('settingapp', '0005_admitcardinfo'),
        ('accounts', '0001_initial'),
        ('talimats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_name', models.CharField(max_length=100)),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_term_madrasha', to='accounts.madrasha')),
            ],
            options={
                'unique_together': {('term_name', 'madrasha')},
            },
        ),
        migrations.CreateModel(
            name='TeacherTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_title', models.CharField(max_length=255)),
                ('training_description', models.TextField()),
                ('madrasha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teacher_training', to='accounts.madrasha')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherStaffResponsibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsibility', models.CharField(max_length=500)),
                ('madrasha', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_responsibility', to='accounts.madrasha')),
                ('teacher_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsible_staffs', to='teachers.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_year', models.CharField(max_length=20)),
                ('syllabus_details', models.TextField()),
                ('syllabus_file', models.FileField(blank=True, null=True, upload_to='syllabus')),
                ('exam_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='syllabus_term', to='talimats.examterm')),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='syllabus_madrasha', to='accounts.madrasha')),
                ('madrasha_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='syllabus_class', to='settingapp.madrashaclasses')),
            ],
        ),
        migrations.CreateModel(
            name='HallDuty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duty_date', models.DateTimeField()),
                ('chief_of_hall', models.CharField(max_length=255)),
                ('assistant_of_hall', models.CharField(blank=True, max_length=255, null=True)),
                ('room_no', models.CharField(max_length=100)),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hall_duty_madrasha', to='accounts.madrasha')),
            ],
        ),
        migrations.CreateModel(
            name='ExtraActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=250)),
                ('duration', models.CharField(max_length=250)),
                ('start_time', models.CharField(max_length=250)),
                ('place', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('managed_by', models.CharField(max_length=250)),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.madrasha')),
            ],
        ),
        migrations.CreateModel(
            name='ExamRoutine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_start_date_time', models.DateTimeField()),
                ('exam_finish_date_time', models.DateTimeField()),
                ('exam_subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='routines_books', to='settingapp.books')),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exam_routine', to='accounts.madrasha')),
                ('routine_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_routine_class', to='settingapp.madrashaclasses')),
                ('routine_term', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='routines_terms', to='talimats.examterm')),
            ],
        ),
        migrations.CreateModel(
            name='ExamRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.TextField(max_length=300)),
                ('is_registered', models.BooleanField(default=False)),
                ('exam_term', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registration_exam_term', to='talimats.examterm')),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exam_registration_madrasha', to='accounts.madrasha')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration_session', to='settingapp.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exam_registration_student', to='students.student')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration_class', to='settingapp.madrashaclasses')),
            ],
        ),
        migrations.CreateModel(
            name='ExamAnnouncement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_title', models.CharField(max_length=255)),
                ('exam_description', models.TextField()),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exam_announcement', to='accounts.madrasha')),
            ],
        ),
        migrations.CreateModel(
            name='Dawah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=250)),
                ('duration', models.CharField(max_length=250)),
                ('start_time', models.CharField(max_length=250)),
                ('place', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('managed_by', models.CharField(max_length=250)),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.madrasha')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_date', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
                ('is_leave', models.BooleanField(default=False)),
                ('is_program', models.BooleanField(default=False)),
                ('is_exam', models.BooleanField(default=False)),
                ('other', models.BooleanField(default=False)),
                ('madrasha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='madrasha_calendar', to='accounts.madrasha')),
            ],
        ),
    ]
