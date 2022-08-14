from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdminView(admin.ModelAdmin):
    list_display = ['student_id', 'birth_certificate']