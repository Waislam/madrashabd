from rest_framework import serializers
from darul_ekama.models import SeatBooking


class SeatBookingSerializer(serializers.ModelSerializer):
    # madrasha students  building floor room seat is_active created_at
    class Meta:
        model = SeatBooking
        fields = '__all__'


class SeatBookingListSerializer(serializers.ModelSerializer):
    # madrasha students  building floor room seat is_active created_at
    class Meta:
        model = SeatBooking
        fields = '__all__'
        depth = 2


