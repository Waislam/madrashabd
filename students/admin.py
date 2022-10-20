from django.contrib import admin
from .models import Student, AcademicFess, Parent


@admin.register(Student)
class StudentAdminView(admin.ModelAdmin):
    list_display = ['student_id', 'birth_certificate']


admin.site.register(AcademicFess)
admin.site.register(Parent)

