from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Order, User, Country, Manufacturer, Product, Cart

class UserRegistrSerializer(serializers.Serializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'password2')

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        user.set_password(password)
        user.save()

        def __init__ (self):
            self.user = user

        return user
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    user: User = None

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        raise serializers.ValidationError("Неверный логин или пароль")

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(many=True)
    country = CountrySerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'manufacturer', 'country', 'is_new', 'price')

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = ('id', 'product', 'user')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'product')