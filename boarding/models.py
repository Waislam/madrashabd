from django.db import models
from accounts.models import Address, Madrasha

MEASUREMENT_CHOICE = (('kg', 'Kg'),
                      ('litre', 'Litre'),
                      ('gm', 'Gm'),
                      )


class BazarItem(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.SET_NULL, related_name='bazarItem_madrasha', null=True)
    bazar_item_name = models.CharField(max_length=250)
    quantity = models.CharField(max_length=250)
    measurement = models.CharField(max_length=10, choices=MEASUREMENT_CHOICE, default='Kg')
    amount = models.CharField(max_length=250)
    consumption = models.CharField(max_length=250)
    total_stock = models.CharField(max_length=250, blank=True, null=True)


class BazarList(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.SET_NULL, related_name='bazarList_madrasha', null=True)
    item = models.ForeignKey(BazarItem, on_delete=models.SET_NULL, related_name='bazarList_item', null=True)
    date = models.DateField(blank=True, null=True)
    total_cost = models.CharField(max_length=250, blank=True, null=True)

    # class Meta:
    #     ordering = ['-date']






