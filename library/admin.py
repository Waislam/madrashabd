from django.contrib import admin
from library.models import LibraryBook


# Register your models here.
@admin.register(LibraryBook)
class LibraryBookAdminView(admin.ModelAdmin):
    list_display = ['madrasha', 'number', 'name', 'part', 'category', 'book_for_class', 'translator', 'publication', 'original_writer', 'language']
