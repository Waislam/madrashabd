from rest_framework import serializers
from .models import (Department, Designation, MadrashaClasses,
                     MadrashaGroup, Shift, Session, Books, Fees,
                     ExamRules)
from accounts.serializers import MadrashaSerializer


# class StatusSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Status
#         fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    # madrasha = MadrashaSerializer()

    class Meta:
        model = Department
        fields = ('id', 'name', 'is_active', 'madrasha', 'slug')


class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields = ('id', 'name', 'is_active', 'madrasha', 'slug')


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = MadrashaClasses
        fields = ('id', 'name', 'department', 'is_active', 'madrasha', 'slug')


class ClassGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = MadrashaGroup
        fields = ('id', 'name', 'department', 'madrasha_class', 'is_active', 'madrasha', 'slug')


class ShiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shift
        fields = ('id', 'name', 'shift_time', 'department', 'madrasha_class', 'is_active', 'madrasha', 'slug')


class SessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = ('id', 'name', 'is_active', 'madrasha', 'slug')


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('id', 'name', 'department', 'madrasha_class', 'is_active', 'madrasha', 'slug')


class FeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fees
        fields = ('id', 'name', 'amount', 'department', 'madrasha_class', 'is_active', 'madrasha', 'slug')


class ExamRulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamRules
        fields = ('id', 'text_input', 'is_active', 'madrasha')