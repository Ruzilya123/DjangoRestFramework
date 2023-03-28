from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsClient, IsGuest, IsAdmin
from rest_framework.authtoken.models import Token
from .models import User, Country, Cart, Tour, Excursion, PersonalCabinet
from .serializers import UserRegistrSerializer, UserSerializer, UserLoginSerializer, CountrySerializer, ExcursionSerializer, TourSerializer, CartSerializer, PersonalCabinetSerializer
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

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_employee(request):
    user = request.user
    serializer = UserSerializer(user, many=True)
    return Response({"employees": serializer.data}, status=status.HTTP_200_OK)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAdmin]

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated, IsClient, IsGuest]
        return [permission() for permission in permission_classes]
    
class ExcursionViewSet(viewsets.ModelViewSet):
    queryset = Excursion.objects.all()
    serializer_class = ExcursionSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated, IsClient]
        return [permission() for permission in permission_classes]

class PersonalCabinetViewSet(viewsets.ModelViewSet):
    queryset = PersonalCabinet.objects.all()
    serializer_class = PersonalCabinetSerializer
    
    def get_permissions(self):
        if self.action in ['destroy']:
            permission_classes = [permissions.IsAuthenticated, IsAdmin]
        elif self.action in ['update']:
            permission_classes = [permissions.IsAuthenticated, IsClient, IsAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated, IsClient]
        return [permission() for permission in permission_classes]

