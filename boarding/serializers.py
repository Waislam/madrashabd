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
            'measurement',
            'amount',
            'consumption',
            'total_stock'
        ]


class BazarListSerializer(serializers.ModelSerializer):
    item = BazarItemSerializer()

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

    def create(self, validated_data):
            item = validated_data.pop('item')

            bazar_item_obj = BazarItem.objects.create(**item)
            Bazar = BazarList.objects.create(item=bazar_item_obj, **validated_data)
            return Bazar


