from django.db import models
from django.template.defaultfilters import slugify
from accounts.models import Madrasha


# Create your models here.
class Committee(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.CASCADE, blank=True, null=True)
    member_name = models.CharField(max_length=255, blank=True, null=True)
    member_designation = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20)

    class Meta:
        unique_together = [['phone_number', 'madrasha']]
        ordering = ['member_name']

    def __str__(self):
        return self.name



