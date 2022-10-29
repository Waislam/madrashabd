"""
1. BookDistribtuinToTeacherSerializer
"""
from rest_framework import serializers
from talimats.models import BookDistributeToTeacher, TeacherTraining


# ==================== 1. BookDistribtuinToTeacherSerializer ============================== #
class BookDistributionToTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookDistributeToTeacher
        fields = '__all__'


class BookDistributionToTeacherListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookDistributeToTeacher
        fields = '__all__'
        depth = 2


class TeacherTrainingSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherTraining
        fields = '__all__'


class TeacherTrainingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherTraining
        fields = '__all__'
        depth = 2
