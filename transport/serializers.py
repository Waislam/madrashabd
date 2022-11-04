from accounts.models import Madrasha
from students.models import Student
from rest_framework import serializers
from .models import (
    VehicleInfo,
    TransportDetail,
)


class VehicleInfoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleInfo
        fields = [
            'id',
            'madrasha',
            'car_number',
            'driver_name',
            'driver_number',
            'route',
            'time',
        ]

        depth = 2


class VehicleInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleInfo
        fields = [
            'id',
            'madrasha',
            'car_number',
            'driver_name',
            'driver_number',
            'route',
            'time',
        ]


class TransportDetailListSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransportDetail
        fields = [
            'id',
            'madrasha',
            'student_id',
            'vehicle',
            'start_time'
        ]

        depth = 2


class TransportDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransportDetail
        fields = [
            'id',
            'madrasha',
            'student_id',
            'vehicle',
            'start_time'
        ]



