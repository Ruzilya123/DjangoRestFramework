from rest_framework import serializers
from .models import Product, Cart

class ProductSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price')

class CartSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Cart
        fields = ('id', 'products')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['total_price'] = instance.total_price()
        return data




