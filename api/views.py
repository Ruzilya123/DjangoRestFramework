from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Film, Producer, Genre, Poster
from .serializers import FilmSerializer, ProducerSerializer, GenreSerializer, PosterSerializer

class FilmList(ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmDetail(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class ProducerList(ListCreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

class ProducerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

class GenreList(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer  

class GenreDetail(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PosterList(ListCreateAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

class PosterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
