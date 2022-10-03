from rest_framework import serializers
from .models import BazarList, BazarItem


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
            'madrasha',
            'item',
            'date',
            'total_cost',
        ]

    def create(self, validated_data):
        item = validated_data.pop('item')
        item_obj = BazarItem.objects.create(**item)
        bazar_list = BazarList.objects.create(item=item_obj, **validated_data)
        return bazar_list



