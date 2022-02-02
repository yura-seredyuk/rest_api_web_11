from rest_framework import viewsets

from .models import Address, UserList
from .serializer import AddressSerializer, UserListSerializer

class UsersViewset(viewsets.ModelViewSet):
    queryset = UserList.objects.all().order_by('id')
    serializer_class = UserListSerializer

class AddressViewset(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer