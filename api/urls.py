from django.urls import path
from .views import ProductView, CartView

urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    path('product/<int:pk>', ProductView.as_view(), name='product'),
    path('cart/', CartView.as_view(), name='carts'),
    path('cart/<int:pk>', CartView.as_view(), name='cart'),
]