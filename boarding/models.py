from django.db import models
from accounts.models import Address, Madrasha


class BazarList(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.SET_NULL, related_name='bazarList_madrasha', null=True)
    date = models.DateField(blank=True, null=True)
    bazar_item_name = models.CharField(max_length=250)
    quantity = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    consumption = models.CharField(max_length=250)
    current_stock = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.bazar_item_name

