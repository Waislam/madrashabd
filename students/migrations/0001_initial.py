# Generated by Django 4.0.6 on 2022-08-26 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settingapp', '0001_initial'),
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicFess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_bill_percent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monthly_tution_percent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('scholarship_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(max_length=150)),
                ('parent_date_of_birth', models.DateField(blank=True, null=True)),
                ('parent_nid', models.CharField(max_length=255)),
                ('occupation', models.CharField(choices=[('teacher', 'Teacher'), ('farmer', 'Farmer'), ('doctor', 'Doctor'), ('police', 'Police'), ('businessman', 'Businessman'), ('govt. employee', 'Govt. employee'), ('non govt. employee', 'Non govt. employee'), ('other', 'Other')], default='null', max_length=50)),
                ('organization_with_designation', models.CharField(max_length=255)),
                ('education', models.CharField(choices=[('literate', 'Literate'), ('ssc/equivalent', 'SSC/equivalent'), ('hsc/equivalent', 'HSC/equivalent'), ('hons/equivalent', 'Hons/equivalent'), ('ma/equivalent', 'M.A./equivalent'), ('higher/equivalent', 'Higher/equivalent')], default='literate', max_length=200)),
                ('contact_number', models.CharField(max_length=15)),
                ('parent_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=255, unique=True)),
                ('student_roll_id', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('date_of_birth', models.DateField()),
                ('age', models.CharField(blank=True, max_length=255, null=True)),
                ('birth_certificate', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('student_nid', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('passport_number', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('nationality', models.CharField(blank=True, choices=[('bangladeshi', 'Bangladeshi'), ('indian', 'Indian'), ('other', 'Other')], default='bangladeshi', max_length=20, null=True)),
                ('religion', models.CharField(blank=True, choices=[('islam', 'Islam'), ('shonaton', 'Shonaton'), ('other', 'Other')], default='islam', max_length=20, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=20, null=True)),
                ('guardian_name', models.CharField(blank=True, max_length=150, null=True)),
                ('guardian_relation', models.CharField(blank=True, choices=[('father', 'Father'), ('mother', 'Mother'), ('brother', 'Brother'), ('sister', 'Sister'), ('auncle', 'Auncle'), ('aunty', 'Aunty'), ('cousin', 'Cousin')], default='father', max_length=20, null=True)),
                ('guardian_occupation', models.CharField(blank=True, choices=[('teacher', 'Teacher'), ('farmer', 'Farmer'), ('doctor', 'Doctor'), ('police', 'Police'), ('businessman', 'Businessman'), ('govt. employee', 'Govt. employee'), ('non govt. employee', 'Non govt. employee'), ('other', 'Other')], default='null', max_length=20, null=True)),
                ('yearly_income', models.CharField(blank=True, max_length=255, null=True)),
                ('guardian_contact', models.CharField(blank=True, max_length=15, null=True)),
                ('guardian_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('other_contact_person', models.CharField(blank=True, max_length=150, null=True)),
                ('other_contact_person_relation', models.CharField(blank=True, choices=[('father', 'Father'), ('mother', 'Mother'), ('brother', 'Brother'), ('sister', 'Sister'), ('auncle', 'Auncle'), ('aunty', 'Aunty'), ('cousin', 'Cousin')], max_length=20, null=True)),
                ('other_contact_person_contact', models.CharField(blank=True, max_length=15, null=True)),
                ('sibling_id', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_institution_name', models.CharField(blank=True, max_length=255, null=True)),
                ('previous_institution_contact', models.CharField(blank=True, max_length=15, null=True)),
                ('previous_started_at', models.DateField(blank=True, null=True)),
                ('previous_ending_at', models.DateField(blank=True, null=True)),
                ('previous_ending_class', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_ending_result', models.CharField(blank=True, max_length=20, null=True)),
                ('board_exam_name', models.CharField(blank=True, choices=[('befak', 'Befak'), ('haya', 'Haya')], default='null', max_length=30, null=True)),
                ('board_exam_registration', models.CharField(blank=True, max_length=50, null=True)),
                ('board_exam_roll', models.CharField(blank=True, max_length=50, null=True)),
                ('board_exam_result', models.CharField(blank=True, max_length=50, null=True)),
                ('admitted_roll', models.CharField(blank=True, max_length=20, null=True)),
                ('student_blood_group', models.CharField(blank=True, max_length=20, null=True)),
                ('special_body_sign', models.CharField(blank=True, max_length=255, null=True)),
                ('talimi_murobbi_name', models.CharField(blank=True, max_length=150, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('academic_fees', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.academicfess')),
                ('admitted_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_students', to='settingapp.madrashaclasses')),
                ('admitted_department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='department_students', to='settingapp.department')),
                ('admitted_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_students', to='settingapp.madrashagroup')),
                ('admitted_session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='session_students', to='settingapp.session')),
                ('admitted_shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shift_students', to='settingapp.shift')),
                ('father_info', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_father', to='students.parent')),
                ('mother_info', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_mother', to='students.parent')),
                ('permanent_address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_permanent_addres', to='accounts.address')),
                ('present_address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_present_addres', to='accounts.address')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
