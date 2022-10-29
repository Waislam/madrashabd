from rest_framework import serializers
from .models import Committee
from accounts.models import Madrasha


class MadrashaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Madrasha
        fields = [
            'id',
        ]


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