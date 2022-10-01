from rest_framework import serializers
from .models import BazarList, BazarItem
from accounts.serializers import MadrashaSerializer


class BazarItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BazarItem
        fields = [
            'id',
            'madrasha',
            'bazar_item_name',
            'quantity',
            'amount',
            'consumption',
            'total_stock'
        ]


class BazarListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BazarList
        fields = [
            'id',
            'madrasha',
            'item',
            'date',
            'total_cost',
        ]
        depth = 1



