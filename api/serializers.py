from rest_framework import serializers
from .models import Order, OrderStatus, Pets, Category, PetType, PetStatus

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetType
        fields = '__all__'

class PetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetStatus
        fields = '__all__'
        

