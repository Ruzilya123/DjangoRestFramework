from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Country, Cart, Tour, Excursion, PersonalCabinet

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'language')

class ExcursionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excursion
        fields = ('id', 'name', 'place', 'time', 'cost')

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('id', 'name', 'country', 'time', 'service', 'count', 'hotel', 'excursion', 'cost')

class PersonalCabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalCabinet
        fields = ('id', 'tour', 'cost', 'time')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'tour')
