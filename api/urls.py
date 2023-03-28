from django.urls import include, path
from . import views

from .models import User

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('login/', views.LoginUserView.as_view()),
    path('register/', views.RegistrUserView.as_view()),
    path('logout/', views.LogOutUserView.as_view()),
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail),
    path('', include(router.urls)),
]
