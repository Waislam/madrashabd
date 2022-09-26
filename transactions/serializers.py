from rest_framework import serializers
from .models import IncomeCategory, IncomeSubCategory, StudentIncome, OtherIncome, AllExpense, ExpenseCategory, \
    ExpenseSubCategory


class IncomeCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeCategory
        fields = '__all__'


class IncomeSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = IncomeSubCategory
        fields = '__all__'


class StudentIncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentIncome
        fields = ['id', 'madrasha', 'category', 'sub_category', 'student_class_id', 'amount', 'for_month', 'for_months',
                  'paid_date', 'receipt_number', 'student_id', 'voucher_name']

    def create(self, validated_data):
        # create Student Income obj
        student_income = StudentIncome.objects.create(**validated_data)
        return student_income

    def update(self, instance, validated_data):
        print(validated_data)
        # get all nested obj
        category = instance.category
        sub_category = instance.sub_category

        # get updated fields value for every nested obj
        category = validated_data.get('category', category)
        category.save()

        sub_category = validated_data.get('sub_category', sub_category)
        sub_category.save()

        # get instance fields
        instance.amount = validated_data.get('amount', instance.amount)
        instance.for_month = validated_data.get('for_month', instance.for_month)
        instance.for_months = validated_data.get('for_months', instance.for_months)

        instance.save()
        return instance


class StudentIncomeListSerializer(serializers.ModelSerializer):
    category = IncomeCategorySerializer()
    sub_category = IncomeSubCategorySerializer()

    class Meta:
        model = StudentIncome
        fields = ['id', 'madrasha', 'category', 'sub_category', 'student_class_id', 'amount', 'for_month', 'for_months',
                  'paid_date', 'receipt_number', 'student_id', 'voucher_name']


class OtherIncomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OtherIncome
        fields = ['id', 'madrasha', 'category', 'sub_category', 'donar_name', 'amount', 'for_month', 'for_months',
                  'paid_date', 'receipt_book_number', 'receipt_page_number', 'receipt_number', 'voucher_name']

    def create(self, validated_data):
        # create Other Income obj
        other_income = OtherIncome.objects.create(**validated_data)
        return other_income

    def update(self, instance, validated_data):
        # get all nested obj
        category = instance.category
        sub_category = instance.sub_category

        # get updated fields value for every nested obj
        category = validated_data.get('category', category)
        category.save()

        sub_category = validated_data.get('sub_category', sub_category)
        sub_category.save()

        # get instance fields
        instance.donar_name = validated_data.get('donar_name', instance.donar_name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.for_month = validated_data.get('for_month', instance.for_month)
        instance.for_months = validated_data.get('for_months', instance.for_months)
        instance.receipt_book_number = validated_data.get('receipt_book_number', instance.receipt_book_number)
        instance.receipt_page_number = validated_data.get('receipt_page_number', instance.receipt_page_number)

        instance.save()
        return instance


class OtherIncomeListSerializer(serializers.ModelSerializer):
    category = IncomeCategorySerializer()
    sub_category = IncomeSubCategorySerializer()

    class Meta:
        model = OtherIncome
        fields = ['id', 'madrasha', 'category', 'sub_category', 'donar_name', 'amount', 'for_month', 'for_months',
                  'paid_date', 'receipt_book_number', 'receipt_page_number', 'receipt_number', 'voucher_name']


class ExpenseCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseCategory
        fields = '__all__'


class ExpenseSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseSubCategory
        fields = '__all__'


class AllExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = AllExpense
        fields = ['id', 'madrasha', 'category', 'sub_category', 'expense_by', 'date', 'for_month', 'for_months',
                  'receipt_number', 'description', 'approved_by', 'amount', 'voucher_name']

    def create(self, validated_data):
        # create Other Income obj
        all_expense = AllExpense.objects.create(**validated_data)
        return all_expense

    def update(self, instance, validated_data):
        # get all nested obj
        category = instance.category
        sub_category = instance.sub_category

        # get updated fields value for every nested obj
        category = validated_data.get('category', category)
        category.save()

        sub_category = validated_data.get('sub_category', sub_category)
        sub_category.save()

        # get instance fields
        instance.expense_by = validated_data.get('expense_by', instance.expense_by)
        instance.for_month = validated_data.get('for_month', instance.for_month)
        instance.for_months = validated_data.get('for_months', instance.for_months)
        instance.receipt_number = validated_data.get('receipt_number', instance.receipt_number)
        instance.description = validated_data.get('description', instance.description)
        instance.approved_by = validated_data.get('approved_by', instance.approved_by)
        instance.amount = validated_data.get('amount', instance.amount)

        instance.save()
        return instance


class AllExpenseListSerializer(serializers.ModelSerializer):
    category = ExpenseCategorySerializer()
    sub_category = ExpenseSubCategorySerializer()

    class Meta:
        model = AllExpense
        fields = ['id', 'madrasha', 'category', 'sub_category', 'expense_by', 'date', 'for_month', 'for_months',
                  'receipt_number', 'description', 'approved_by', 'amount', 'voucher_name']