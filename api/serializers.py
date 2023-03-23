from rest_framework import serializers
from .models import Book, OrderedBook

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class OrderedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedBook
        fields = '__all__'