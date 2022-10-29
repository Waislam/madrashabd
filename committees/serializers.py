from rest_framework import serializers
from .models import Committee


class CommitteeListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Committee
        fields = [
            'id',
            'madrasha',
            'member_name',
            'member_designation',
            'phone_number'
        ]

        depth = 2


class CommitteeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Committee
        fields = [
            'id',
            'madrasha',
            'member_name',
            'member_designation',
            'phone_number'
        ]
