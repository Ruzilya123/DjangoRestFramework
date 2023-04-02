from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'), # В кавычках указываем путь, а в круглых скобках указываем view, которую мы хотим использовать
    path('register/', views.RegisterUserView.as_view()),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('products/', views.ProductListView.as_view()),
    path('products/<int:pk>/', views.ProductDetailView.as_view()),
    path('carts/', views.CartListView.as_view()),
    path('carts/<int:pk>/', views.CartDetailView.as_view()),
    path('orders/', views.OrderListCreateView.as_view()),
    path('orders/<int:pk>/', views.OrderDetailView.as_view()),
]
