from rest_framework import serializers
from .models import Order, Workers, Position

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'table', 'worker', 'order_start_time', 'status', 'price')

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ('id', 'name', 'surname', 'middle_name', 'login', 'password', 'photo', 'position')

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'position')
        