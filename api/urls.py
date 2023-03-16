
from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_list),
    path('order/<int:pk>/', views.order_detail),
    path('workers/', views.workers_list),
    path('workers/<int:pk>/', views.workers_detail),
    
]