"""
1. address serializer
2. madrasha serializer
3. User
4. User

"""
from rest_framework import serializers
from accounts.models import (Division, District, Thana, PostOffice, PostCode, Address,
                             Madrasha)


# ======= 1. address serializer ================


class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = '__all__'


class ThanaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thana
        fields = '__all__'


class PostOfficeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostOffice
        fields = '__all__'


class PostCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCode
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    division = DivisionSerializer()
    district = DistrictSerializer()
    thana = ThanaSerializer()
    post_office = PostOfficeSerializer()
    post_code = PostCodeSerializer()

    class Meta:
        model = Address
        fields = ('id', 'division', 'district', 'thana', 'post_office', 'post_code', 'address_info')


# ============ 2. madrasha serializer =============


class MadrashaSerializer(serializers.ModelSerializer):
    madrasha_address = AddressSerializer()

    class Meta:
        model = Madrasha
        fields = ('id', 'name', 'madrasha_id', 'madrasha_address', 'created_by', 'updated_by', 'active_status', 'slug')

    # def create(self, validated_data):
    #     print(validated_data)
    #     tracks_data = validated_data.pop('madrasha_address')
    #     # aalbum = M.objects.create(**validated_data)
    #     # for track_data in tracks_data:
    #     #     Track.objects.create(album=album, **track_data)
    #     # return album4
    #     print(tracks_data)
    #     return tracks_data


# ================== 3. User ============



# ================== 4.  ============