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
        fields = ["pk"]


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ["pk"]


class ThanaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thana
        fields = ["pk"]


class PostOfficeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostOffice
        fields = ["pk"]


class PostCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCode
        fields = ["pk"]


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'division', 'district', 'thana', 'post_office', 'post_code', 'address_info']


class NewAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'division', 'district', 'thana', 'post_office', 'post_code', 'address_info']


# ============ 2. madrasha serializer =============


class MadrashaSerializer(serializers.ModelSerializer):
    madrasha_address = AddressSerializer()

    class Meta:
        model = Madrasha
        fields = ['id', 'name', 'madrasha_id', 'madrasha_address', 'created_by', 'updated_by', 'active_status', 'slug']

    def create(self, validated_data):
        madrasha_name = validated_data['name']
        madrasha_id = validated_data['madrasha_id']
        slug = validated_data['slug']

        # create address
        address = Address.objects.create(**validated_data['madrasha_address'])

        # create madrasha
        madrasha = Madrasha.objects.create(
            name=madrasha_name,
            madrasha_address=address,
            madrasha_id=madrasha_id,
            slug=slug
        )

        return madrasha

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.address = validated_data.get('madrasha_address')

        # Get madrasha address
        madrasha_address = Address.objects.get(pk=instance.madrasha_address.pk)

        # Save madrasha address
        madrasha_address.division = validated_data.get('madrasha_address').get('division')
        madrasha_address.district = validated_data.get('madrasha_address').get('district')
        madrasha_address.post_office = validated_data.get('madrasha_address').get('post_office')
        madrasha_address.post_code = validated_data.get('madrasha_address').get('post_code')
        madrasha_address.thana = validated_data.get('madrasha_address').get('thana')
        madrasha_address.address_info = validated_data.get('madrasha_address').get('address_info')
        madrasha_address.save()

        instance.created_by = validated_data.get('created_by')
        instance.updated_by = validated_data.get('updated_by')
        instance.active_status = validated_data.get('active_status')
        instance.save()

        return instance


# ================== 3. User ============



# ================== 4.  ============