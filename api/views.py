from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsClient, IsGuest, IsAdmin
from rest_framework.authtoken.models import Token
from .models import User, Comment, Category, Actor, Genre, Film 
from .serializers import UserRegistrSerializer, UserSerializer, UserLoginSerializer, CategorySerializer, ActorSerializer, GenreSerializer, FilmSerializer, CommentSerializer
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
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse({'error': {
                'code': 400,
                'non_field_errors': 'Unable to log in with provided credentials'
            }}, status=400)
        user = serializer.validated_data
        if user:
            token_object, token_created = Token.objects.get_or_create(user=user)
            token = token_object if token_object else token_created
            return Response({'user_token': token.key}, status=status.HTTP_200_OK)
        return Response({
            'non_field_errors': {
                'message': 'Unable to log in with provided credentials'
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

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsClient]

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated, IsClient, IsGuest]
        return [permission() for permission in permission_classes]

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAdmin]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdmin]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]
