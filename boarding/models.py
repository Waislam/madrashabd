from django.db import models
from accounts.models import Address, Madrasha


class BazarItem(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.SET_NULL, related_name='bazarItem_madrasha', null=True)
    bazar_item_name = models.CharField(max_length=250)
    quantity = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    consumption = models.CharField(max_length=250)
    total_stock = models.CharField(max_length=250, blank=True, null=True)


class BazarList(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.SET_NULL, related_name='bazarList_madrasha', null=True)
    item = models.ForeignKey(BazarItem, on_delete=models.SET_NULL, related_name='bazarList_item', null=True)
    date = models.DateField(blank=True, null=True)
    total_cost = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']






