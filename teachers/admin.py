from django.contrib import admin
from .models import Teacher

# Register your models here.
@admin.register(Teacher)
class TeacherAdminView(admin.ModelAdmin):
    list_display = ['teacher_id', 'slug']