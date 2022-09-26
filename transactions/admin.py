from django.contrib import admin
from .models import (IncomeCategory,
                     IncomeSubCategory,
                     StudentIncome,
                     OtherIncome,
                     ExpenseCategory,
                     ExpenseSubCategory,
                     AllExpense
                     )

# Register your models here.

admin.site.register(IncomeCategory)
admin.site.register(IncomeSubCategory)


@admin.register(StudentIncome)
class StudentIncomeAdminView(admin.ModelAdmin):
    list_display = ['category', 'sub_category', 'student_class_id']

    class Media:
        js = ("js/incomecategorydependable.js",)


@admin.register(OtherIncome)
class OtherIncomeAdminView(admin.ModelAdmin):
    list_display = ['donar_name']

    class Media:
        js = ("js/incomecategorydependable.js",)


admin.site.register(ExpenseCategory)
admin.site.register(ExpenseSubCategory)


@admin.register(AllExpense)
class AllExpenseAdminView(admin.ModelAdmin):
    list_display = ['madrasha']

    class Media:
        js = ("js/expensedropdowncategory.js",)