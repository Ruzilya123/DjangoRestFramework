from django.urls import path
from .views import FilmList, FilmDetail, ProducerList, ProducerDetail, GenreList, GenreDetail, PosterList, PosterDetail

urlpatterns = [
    path('films/', FilmList.as_view()),
    path('films/<int:pk>/', FilmDetail.as_view()),
    path('producers/', ProducerList.as_view()),
    path('producers/<int:pk>/', ProducerDetail.as_view()),
    path('genres/', GenreList.as_view()),
    path('genres/<int:pk>/', GenreDetail.as_view()),
    path('posters/', PosterList.as_view()),
    path('posters/<int:pk>/', PosterDetail.as_view()),
]