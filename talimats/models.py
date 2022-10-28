"""
1. Book Distribution to Teacher
"""

from django.db import models
from accounts.models import Madrasha
from settingapp.models import MadrashaClasses


# Create your models here.
# ================== 1. Book Distribution to Teacher ===============#


class BookDistributeToTeacher(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.CASCADE, related_name="books_to_teacher", blank=True, null=True)
    teacher_name = models.CharField(max_length=255)
    kitab_name = models.CharField(max_length=255)
    class_name = models.ForeignKey(MadrashaClasses, on_delete=models.SET_NULL, related_name="book_to_class", blank=True, null=True)
    class_time = models.CharField(max_length=255)

    def __str__(self):
        return self.kitab_name


