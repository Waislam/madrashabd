from rest_framework import serializers
from .models import (Department, Designation, MadrashaClasses,
                     MadrashaGroup, Shift, Session, Books, Fees,
                     ExamRules, Status)
from accounts.serializers import MadrashaSerializer


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    madrasha = MadrashaSerializer()

    class Meta:
        model = Department
        fields = ('id', 'name', 'status', 'madrasha', 'slug')


class DesignationSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    madrasha = MadrashaSerializer()

    class Meta:
        model = Designation
        fields = ('id', 'name', 'status', 'madrasha', 'slug')


class ClassSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    status = StatusSerializer()
    madrasha = MadrashaSerializer()

    class Meta:
        model = MadrashaClasses
        fields = ('id', 'name', 'department', 'status', 'madrasha', 'slug')


class ClassGroupSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    madrasha_class = ClassSerializer()
    status = StatusSerializer()
    madrasha = MadrashaSerializer()

    class Meta:
        model = MadrashaGroup
        fields = ('id', 'name', 'department', 'madrasha_class', 'status', 'madrasha', 'slug')


class ShiftSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    madrasha_class = ClassSerializer()
    status = StatusSerializer()
    madrasha = MadrashaSerializer()

    class Meta:
        model = Shift
        fields = ('id', 'name', 'shift_time', 'department', 'madrasha_class', 'status', 'madrasha', 'slug')


class SessionSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    madrasha = MadrashaSerializer()

    class Meta:
        model = Session
        fields = ('id', 'name', 'status', 'madrasha', 'slug')


class BooksSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    madrasha_class = ClassSerializer()
    status = StatusSerializer()
    madrasha = MadrashaSerializer()

    class Meta:
        model = Books
        fields = ('id', 'name', 'department', 'madrasha_class', 'status', 'madrasha', 'slug')


class FeesSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    madrasha_class = ClassSerializer()
    status = StatusSerializer()
    madrasha = MadrashaSerializer()

    class Meta:
        model = Fees
        fields = ('id', 'name', 'amount', 'department', 'madrasha_class', 'status', 'madrasha', 'slug')


class ExamRulesSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    madrasha = MadrashaSerializer()

    class Meta:
        model = ExamRules
        fields = ('id', 'text_input', 'status', 'madrasha', 'slug')