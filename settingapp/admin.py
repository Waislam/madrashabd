from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(MadrashaClasses)
admin.site.register(MadrashaGroup)
admin.site.register(Shift)
admin.site.register(Session)
admin.site.register(Fees)
admin.site.register(ExamRules)