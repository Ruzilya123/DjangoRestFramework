from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Category, Actor, Genre, Film, Comment

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
        raise serializers.ValidationError("Unable to log in with provided credentials")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'age', 'description', 'photo')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'description')

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'name', 'description', 'poster', 'date_out', 'country', 'actor', 'genre', 'category')

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'movie', 'text')

