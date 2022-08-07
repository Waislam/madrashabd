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
        fields = ('id', 'name', 'madrasha_id', 'madrasha_address', 'madrasha_logo', 'created_by', 'updated_by', 'active_status', 'slug')


# ================== 3. User ============



# ================== 4.  ============