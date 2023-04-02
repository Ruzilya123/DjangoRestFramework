from django.contrib.auth import logout
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .models import Product, Cart, Order, User
from .permissions import IsAdmin, IsClient, IsGuest
from .serializers import ProductSerializer, CartSerializer, OrderSerializer, UserRegisterSerializer, UserLoginSerializer
from .authentication import BearerAuthentication

class RegisterUserView(ListCreateAPIView):
    queryset = User.objects.all() # queryset - это то, что мы будем сериализовать, в данном случае это все пользователи
    serializer_class = UserRegisterSerializer # Сериализатор, который мы будем использовать
    authentication_classes = [BearerAuthentication] # Аутентификация, которую мы будем использовать

    def post(self, request, *args, **kwargs): # Метод для создания пользователя
        serializer = UserRegisterSerializer(data=request.data) # Создаем сериализатор с данными, которые мы получили
        if serializer.is_valid(): # Если сериализатор валидный
            user = serializer.save() # Сохраняем пользователя
            token = Token.objects.create(user=user) # Создаем токен для пользователя
            return Response({'token': token.key}, status=status.HTTP_200_OK) # Возвращаем токен
        else:
            return Response(serializer.errors) # Иначе возвращаем ошибки

class LoginUserView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data # Валидируем данные
            token, _ = Token.objects.get_or_create(user=user) # Получаем или создаем токен для пользователя
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)

class LogoutUserView(APIView):
    permission_classes = [IsClient] # Указываем, что пользователь должен быть клиентом

    def post(self, request): # Метод для выхода пользователя
        request.user.auth_token.delete() # Удаляем токен
        logout(request) # Выходим из системы
        return Response(status=status.HTTP_200_OK)

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs): # Метод для создания товара
        if not request.user.is_staff: # Если пользователь не является администратором
            return Response(status=status.HTTP_403_FORBIDDEN) # Возвращаем ошибку

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsClient]

class CartListView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsClient]

class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsClient]

class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsClient]

