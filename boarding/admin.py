from django.contrib import admin
from .models import BazarItem, BazarList


class BazarItemAdmin(admin.ModelAdmin):
    list_display = ['quantity']
    list_per_page = 30

    class Meta:
        model = BazarItem


admin.site.register(BazarItem, BazarItemAdmin)


class BazarListAdmin(admin.ModelAdmin):
    list_display = ['date']
    list_per_page = 30

    class Meta:
        model = BazarList


admin.site.register(BazarList, BazarListAdmin)



