from rest_framework import viewsets

from .models import Order, OrderStatus, Pets, Category, PetType, PetStatus
from .serializers import OrderSerializer, OrderStatusSerializer, PetsSerializer, CategorySerializer, PetTypeSerializer, PetStatusSerializer

class OrderList(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderStatusList(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

class OrderStatusDetail(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

class PetsList(viewsets.ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer

class PetsDetail(viewsets.ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer

class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PetTypeList(viewsets.ModelViewSet):
    queryset = PetType.objects.all()
    serializer_class = PetTypeSerializer

class PetTypeDetail(viewsets.ModelViewSet):
    queryset = PetType.objects.all()
    serializer_class = PetTypeSerializer

class PetStatusList(viewsets.ModelViewSet):
    queryset = PetStatus.objects.all()
    serializer_class = PetStatusSerializer

class PetStatusDetail(viewsets.ModelViewSet):
    queryset = PetStatus.objects.all()
    serializer_class = PetStatusSerializer

