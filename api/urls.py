from django.urls import include, path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies', views.FilmViewSet)
router.register('review', views.CommentsViewSet)
router.register('cat', views.CategoryViewSet)
router.register('actors', views.ActorViewSet)

urlpatterns = [
    path('login/', views.LoginUserView.as_view()),
    path('register/', views.RegistrUserView.as_view()),
    path('logout/', views.LogOutUserView.as_view()),
    path('', include(router.urls)),
]
