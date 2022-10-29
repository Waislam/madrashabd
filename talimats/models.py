"""
1. Book Distribution to Teacher
"""

from django.db import models
from accounts.models import Madrasha
from settingapp.models import MadrashaClasses, Books

from teachers.models import Teacher
from students.models import Student


# Create your models here.
# ================== 1. Book Distribution to Teacher ===============#


class BookDistributeToTeacher(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.CASCADE, related_name="books_to_teacher", blank=True,
                                 null=True)
    teacher_name = models.CharField(max_length=255)
    kitab_name = models.CharField(max_length=255)
    class_name = models.ForeignKey(MadrashaClasses, on_delete=models.SET_NULL, related_name="book_to_class", blank=True,
                                   null=True)
    class_time = models.CharField(max_length=255)

    def __str__(self):
        return self.kitab_name


class TeacherTraining(models.Model):
    madrasha = models.ForeignKey(
        Madrasha,
        on_delete=models.PROTECT,
        related_name='teacher_training',
        blank=True,
        null=True
    )
    training_title = models.CharField(max_length=255)
    training_description = models.TextField()

    def __str__(self):
        return self.training_title


class ExamTerm(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.CASCADE, related_name="exam_term_madrasha")
    term_name = models.CharField(max_length=100)

    class Meta:
        unique_together = [['term_name', 'madrasha']]

    def __str__(self):
        return self.term_name


class Syllabus(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.CASCADE, related_name="syllabus_madrasha")
    madrasha_class = models.ForeignKey(MadrashaClasses, on_delete=models.PROTECT, related_name='syllabus_class')
    exam_term = models.ForeignKey(ExamTerm, on_delete=models.CASCADE, related_name='syllabus_term')
    session_year = models.CharField(max_length=20)  # readly only from anywhere
    syllabus_details = models.TextField()
    syllabus_file = models.FileField(upload_to='syllabus', blank=True, null=True)

    def __str__(self):
        return self.exam_term.term_name


class TeacherStaffResponsibility(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.SET_NULL, related_name="staff_responsibility", null=True,
                                 blank=True)
    teacher_staff = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="responsible_staffs")
    responsibility = models.CharField(max_length=500)

    def __str__(self):
        return self.teacher_staff.teacher_id


class AcademicCalendar(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.CASCADE, related_name="madrasha_calendar")
    calendar_date = models.DateTimeField()
    description = models.CharField(max_length=500)
    is_leave = models.BooleanField(default=False)
    is_program = models.BooleanField(default=False)
    is_exam = models.BooleanField(default=False)
    other = models.BooleanField(default=False)

    def __str__(self):
        return str(self.calendar_date)


class ExamAnnouncement(models.Model):
    madrasha = models.ForeignKey(
        Madrasha,
        on_delete=models.PROTECT,
        related_name='exam_announcement'
    )
    exam_title = models.CharField(max_length=255)
    exam_description = models.TextField()

    def __str__(self):
        return self.exam_title


class ExamRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='exam_registration_student')
    amount = models.TextField(max_length=300)
    exam_term = models.ForeignKey(ExamTerm, on_delete=models.PROTECT, related_name='registration_exam_term')
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return self.student.student_id


class ExamRoutine(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='exam_routine')
    routine_class = models.ForeignKey(MadrashaClasses, on_delete=models.CASCADE, related_name='exam_routine_class')
    exam_start_date_time = models.DateTimeField()
    exam_finish_date_time = models.DateTimeField()
    exam_subject = models.ForeignKey(Books, on_delete=models.PROTECT, related_name='routines_books')
    routine_term = models.ForeignKey(ExamTerm, on_delete=models.PROTECT, related_name='routines_terms')

    def __str__(self):
        return self.routine_class
