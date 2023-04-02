from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Product, Cart, Order, User

class UserRegisterSerializer(serializers.ModelSerializer): # ModelSerializer чтобы не писать каждый раз поля
    # Поля для подтверждения пароля, которые не будут сохраняться в базу данных
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta: # Мета класс для сериализатора
        model = User # Модель, которую мы сериализуем
        fields = ('email', 'password', 'password2', 'fio', 'gender') # Поля, которые мы сериализуем
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data): # Метод для валидации данных
        if data['password'] != data['password2']: # Если пароли не совпадают
            raise serializers.ValidationError("Passwords must match") # Возвращаем ошибку
        return data # Возвращаем данные
    
    def create(self, validated_data): # Метод для создания пользователя
        del validated_data['password2'] # Удаляем поле для подтверждения пароля
        validated_data['username'] = validated_data['email'] # Переименовываем поле username
        user = User.objects.create_user(**validated_data) # Создаем пользователя
        return user # Возвращаем пользователя
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField() # Поле для ввода логина
    password = serializers.CharField() # Поле для ввода пароля

    def validate(self, data): # Метод для валидации данных
        user = authenticate(**data) # Проверяем пользователя
        if user and user.is_active: # Если пользователь существует и активен
            return user # Возвращаем пользователя
        raise serializers.ValidationError("Incorrect Credentials") # Иначе возвращаем ошибку

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # Все поля

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.IntegerField(required=False) # Поле для общей цены заказа должно быть необязательным

    class Meta:
        model = Order
        fields = '__all__'
    
    def save(self, **kwargs): # Метод для сохранения заказа
        total_price = 0 # Общая цена
        for product in self.validated_data['product']: # Проходимся по всем продуктам в заказе
            total_price += product.price # Добавляем цену продукта к общей цене
        self.validated_data['total_price'] = total_price # Добавляем общую цену к данным
        super().save(**kwargs) # Сохраняем заказ