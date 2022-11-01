from django.contrib import admin
from talimats.models import BookDistributeToTeacher, ExamAnnouncement, ExamRegistration, ExamTerm, HallDuty


# Register your models here.
@admin.register(BookDistributeToTeacher)
class BookDistributeToTeacherAdminView(admin.ModelAdmin):
    list_display = ['kitab_name', 'teacher_name', 'madrasha', 'class_name', 'class_time']


admin.site.register(ExamAnnouncement)
admin.site.register(ExamRegistration)
admin.site.register(ExamTerm)
admin.site.register(HallDuty)
