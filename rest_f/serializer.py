from pprint import pprint
from rest_framework import serializers
from .models import UserList, Address
from .validator import AddressValidator


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'country', 'city', 'zip_code', 'street', 'house_num', 'apartaments']
        validators = [AddressValidator()]

    def create(self, validated_data):
        address = Address.objects.filter(**validated_data)
        if address:
            raise serializers.ValidationError("Serializer error: Address with this data is already exixts.")
        rezult = Address.objects.create(**validated_data)
        return rezult

    def update(self, instance, validated_data):
        address = Address.objects.filter(**validated_data)
        if address:
            if instance == address[0]:
                print("Serializer message: None fields was changed.")
                return instance
            else:
                raise serializers.ValidationError("Serializer error: Address with this data is already exixts.")
        

        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.zip_code = validated_data.get('zip_code', instance.zip_code)
        instance.street = validated_data.get('street', instance.street)
        instance.house_num = validated_data.get('house_num', instance.house_num)
        instance.apartaments = validated_data.get('apartaments', instance.apartaments)
        instance.save()
        return instance

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ['id', 'username', 'email', 'address']