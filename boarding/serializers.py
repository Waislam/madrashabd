from rest_framework import serializers
from .models import BazarList
from accounts.serializers import MadrashaSerializer


class BazarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BazarList
        fields = [
            'id',
            'madrasha',
            'date',
            'bazar_item_name',
            'quantity',
            'amount',
            'consumption'
        ]
