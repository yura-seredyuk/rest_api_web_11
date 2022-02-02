from dataclasses import fields
from pprint import pprint
from pyexpat import model
from rest_framework import serializers
from .models import UserList, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'country', 'city', 'zip_code', 'street', 'house_num', 'apartaments']

    def create(self, validated_data):
        # pprint(validated_data)
        rezult = Address.objects.create(**validated_data)
        # print(rezult.id)
        return rezult

    def update(self, instance, validated_data):
        pass

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ['id', 'username', 'email', 'address']