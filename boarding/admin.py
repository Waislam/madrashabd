from django.contrib import admin
from .models import BazarList


class BazarListAdmin(admin.ModelAdmin):
    list_display = ['date', 'bazar_item_name', 'amount']
    list_per_page = 30

    class Meta:
        model = BazarList


admin.site.register(BazarList, BazarListAdmin)
