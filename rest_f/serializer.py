from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import UserList, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'country', 'city', 'zip_code', 'house_num', 'apartaments']
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ['id', 'username', 'email', 'address']