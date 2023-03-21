from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'products', 'total_price')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'products')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

__all__ = ['ProductSerializer', 'OrderSerializer', 'CartSerializer', 'UserSerializer']
