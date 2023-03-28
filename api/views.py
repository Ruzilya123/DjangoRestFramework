from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from .models import User, Country, Manufacturer, Product, Cart
from .serializers import UserRegistrSerializer, UserLoginSerializer, CountrySerializer, ManufacturerSerializer, ProductSerializer, CartSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

class RegistrUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['data'] = serializer.data
            user = serializer.user
            token = Token.objects.get(user=user).key
            print(Token)
            return Response({'user_token': token.key}, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

def hello(request):
    return JsonResponse({'data': {'message': 'Hello world!'}})


class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse({'error': {
                'code': 400,
                'message': 'Authentification failed'
            }}, status=400)
        user = serializer.validated_data
        if user:
            token_object, token_created = Token.objects.get_or_create(user=user)
            token = token_object if token_object else token_created
            return Response({'user_token': token.key}, status=status.HTTP_200_OK)
        return Response({
            'error': {
                'message': 'Authentification failed'
            }
        })
    def get(self, request, *args, **kwargs):
        return Response({
            'data': {
                'message': 'Authentification'
            }
        }, status=200)
    
class LogOutUserView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            return JsonResponse({
                'error': {
                    'code': 401,
                    'message': 'Logout failed'
                }
            }, status=401)
        logout(request)
        return JsonResponse({
            'data': {
                'message': 'Logout'
            }
        }, status=200)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdminUser]

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAdminUser]

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        product.delete()
        return Response({'deleted': True})

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

