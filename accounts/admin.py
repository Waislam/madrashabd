from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Address)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('division', 'district', 'thana', 'post_office', 'post_code')

    class Media:
        js = ("js/dependable_dropdown_address_ajax.js",)


admin.site.register(Division)
admin.site.register(District)
admin.site.register(Thana)
admin.site.register(PostOffice)
admin.site.register(PostCode)


admin.site.register(Role)

admin.site.register(CustomUser)


@admin.register(Madrasha)
class MadrashaModel(admin.ModelAdmin):
    list_display = ('name', 'madrasha_id', 'madrasha_address', 'madrasha_logo', 'created_at', 'updated_at', 'created_by', 'updated_by', 'active_status')


@admin.register(MadrashaUserListing)
class MadrashaUserListAdmin(admin.ModelAdmin):
    list_display = ('user', 'madrasha')



# @admin.register(Address)
# class AddressModel()
