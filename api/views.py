from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .models import Film, Producer, Genre, Poster
from .serializers import FilmSerializer, ProducerSerializer, GenreSerializer, PosterSerializer

class FilmList(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class FilmDetail(RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class ProducerList(ListAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

class ProducerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

class GenreList(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer  

class GenreDetail(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PosterList(ListAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer

class PosterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
