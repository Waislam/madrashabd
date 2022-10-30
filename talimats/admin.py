from django.contrib import admin
from talimats.models import BookDistributeToTeacher, Dawah


# Register your models here.
@admin.register(BookDistributeToTeacher)
class BookDistributeToTeacherAdminView(admin.ModelAdmin):
    list_display = ['kitab_name', 'teacher_name', 'madrasha', 'class_name', 'class_time']


# Register your models here.
@admin.register(Dawah)
class DawahAdminView(admin.ModelAdmin):
    list_display = ['program_name', 'duration', 'start_Time', 'managed_by']