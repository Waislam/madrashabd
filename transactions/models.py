"""
1. Income part
2. Expense part
"""


from django.db import models
from accounts.models import Madrasha
from settingapp.models import Fees
from django.contrib.auth import get_user_model
from datetime import date

from students.models import Student

User = get_user_model()

# Create your models here.

# ================================ 1. Income part ====================== #

MONTH_CHOICES = (('null', 'Null'),
                 ('january', 'January'),
                 ('february', 'February'),
                 ('march', 'March'),
                 ('april', 'April'),
                 ('may', 'May'),
                 ('june', 'June'),
                 ('july', 'July'),
                 ('august', 'August'),
                 ('september', 'September'),
                 ('october', 'October'),
                 ('november', 'November'),
                 ('december', 'December'))


class IncomeCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class IncomeSubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(IncomeCategory, on_delete=models.SET_NULL, related_name='sub_categories', null=True)

    def __str__(self):
        return self.name


class StudentIncome(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='students_incomes', null=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.PROTECT, related_name='categories', null=True)
    sub_category = models.ForeignKey(IncomeSubCategory, on_delete=models.PROTECT, related_name='sub_categories', null=True)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='student_payment')
    amount = models.ForeignKey(Fees, on_delete=models.SET_NULL, related_name='amounts', null=True)
    for_month = models.CharField(max_length=20, choices=MONTH_CHOICES, null=True, blank=True)
    for_months = models.CharField(max_length=100, null=True, blank=True)
    paid_date = models.DateField(default=date.today)
    receipt_number = models.CharField(max_length=20, blank=True)  ## autogenerated
    # student_id = models.CharField(max_length=30, blank=True)  #auto from student model st101
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='st_incomes', blank=True, null=True)
    updated_cat = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='updated_st_icomes', blank=True, null=True, editable=False)
    voucher_name = models.CharField(max_length=50, blank=True)

    def generate_receipt_number(self):
        today_date = date.today()
        year = str(today_date.year)
        start_from = 1
        last_obj = StudentIncome.objects.last()
        if last_obj:
            receipt_number = last_obj.receipt_number  # string value
            last_receipt_number = int(receipt_number[4:])
        else:
            last_receipt_number = start_from
        new_number = str(last_receipt_number + 1)
        new_receipt_number = year + new_number
        return new_receipt_number

    def save(self, *args, **kwargs):
        if not self.receipt_number:
            self.receipt_number = self.generate_receipt_number()
        if not self.voucher_name:
            self.voucher_name = "Student Income voucher"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.student_class_id


class OtherIncome(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='other_incomes', null=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.PROTECT, related_name='categories_others', null=True)
    sub_category = models.ForeignKey(IncomeSubCategory, on_delete=models.PROTECT, related_name='sub_categories_others', null=True)
    donar_name = models.CharField(max_length=200)
    amount = models.CharField(max_length=15)
    for_month = models.CharField(max_length=15, choices=MONTH_CHOICES, null=True, blank=True)
    for_months = models.CharField(max_length=100, null=True, blank=True)
    paid_date = models.DateField(default=date.today)
    receipt_book_number = models.CharField(max_length=50, blank=True, null=True)
    receipt_page_number = models.CharField(max_length=50, blank=True, null=True)
    receipt_number = models.CharField(max_length=20, blank=True)  ## autogenerated
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='other_incomes', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='updated_other_incomes', blank=True,null=True, editable=False)
    voucher_name = models.CharField(max_length=50, blank=True)

    def generate_receipt_number(self):
        today_date = date.today()
        year = str(today_date.year)
        start_from = 1
        last_obj = OtherIncome.objects.last()
        if last_obj:
            receipt_number = last_obj.receipt_number  # string value
            last_receipt_number = int(receipt_number[4:])
        else:
            last_receipt_number = start_from
        new_number = str(last_receipt_number + 1)
        new_receipt_number = year + new_number
        return new_receipt_number

    def save(self, *args, **kwargs):
        if not self.receipt_number:
            self.receipt_number = self.generate_receipt_number()
        if not self.voucher_name:
            self.voucher_name = "Other Income voucher"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.donar_name


# ============================ 2. Expense part =================== #

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ExpenseSubCategory(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, related_name='expense_sub_cats', null=True)

    def __str__(self):
        return self.name


class AllExpense(models.Model):
    madrasha = models.ForeignKey(Madrasha, on_delete=models.PROTECT, related_name='allexpenses', null=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.PROTECT, related_name='expense_categories', null=True)
    sub_category = models.ForeignKey(ExpenseSubCategory, on_delete=models.PROTECT, related_name='expense_sub_categories', null=True)
    expense_by = models.CharField(max_length=250, default='')
    date = models.DateField(default=date.today)
    for_month = models.CharField(max_length=15, choices=MONTH_CHOICES, blank=True, null=True)
    for_months = models.CharField(max_length=100, null=True, blank=True)
    receipt_number = models.CharField(max_length=20, blank=True)  ## autogenerated voucher_number
    description = models.CharField(max_length=255, default='')
    approved_by = models.CharField(max_length=255, default='')
    amount = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='expenses', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='updated_expenses', blank=True, null=True, editable=False)
    voucher_name = models.CharField(max_length=50, blank=True)

    def generate_receipt_number(self):
        today_date = date.today()
        year = str(today_date.year)
        start_from = 1
        last_obj = OtherIncome.objects.last()
        if last_obj:
            receipt_number = last_obj.receipt_number  # starting value
            last_receipt_number = int(receipt_number[4:])
        else:
            last_receipt_number = start_from
        new_number = str(last_receipt_number + 1)
        new_receipt_number = year + new_number
        return new_receipt_number

    def save(self, *args, **kwargs):
        if not self.receipt_number:
            self.receipt_number = self.generate_receipt_number()
        if not self.voucher_name:
            self.voucher_name = "Expense voucher"
        super(AllExpense, self).save(*args, **kwargs)

    def __str__(self):
        return self.sub_category.name
