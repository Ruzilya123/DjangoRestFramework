from django.urls import include, path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>/', views.OrderDetail.as_view()),
    path('carts/', views.CartList.as_view()),
    path('carts/<int:pk>/', views.CartDetail.as_view()),
]
