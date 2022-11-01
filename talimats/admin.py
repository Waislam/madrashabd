from django.contrib import admin
from talimats.models import (
    BookDistributeToTeacher,
    Dawah,
    ExtraActivity,
    ExamAnnouncement,
    ExamRegistration,
    ExamTerm,
    HallDuty
)


# Register your models here.
@admin.register(BookDistributeToTeacher)
class BookDistributeToTeacherAdminView(admin.ModelAdmin):
    list_display = ['kitab_name', 'teacher_name', 'madrasha', 'class_name', 'class_time']


# Register your models here.
@admin.register(Dawah)
class DawahAdminView(admin.ModelAdmin):
    list_display = ['program_name', 'duration', 'start_time', 'managed_by']


# Register your models here.
@admin.register(ExtraActivity)
class ExtraActivityView(admin.ModelAdmin):
    list_display = ['category', 'duration', 'start_time', 'managed_by']


admin.site.register(ExamAnnouncement)
admin.site.register(ExamRegistration)
admin.site.register(ExamTerm)
admin.site.register(HallDuty)
