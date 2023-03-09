from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'orders', views.OrderList, basename='orders')
router.register(r'orderstatus', views.OrderStatusList, basename='orderstatus')
router.register(r'pets', views.PetsList, basename='pets')
router.register(r'category', views.CategoryList, basename='category')
router.register(r'pettype',views. PetTypeList, basename='pettype')
router.register(r'petstatus', views.PetStatusList, basename='petstatus')

urlpatterns = [
    path('', include(router.urls)),
]