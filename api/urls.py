from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('group_list/', views.group_list),
    path('group_list_detail/<int:pk>/', views.group_list_detail),
    path('staff_list/', views.staff_list),
    path('staff_list_detail/<int:pk>/', views.staff_list_detail),
    path('product_list/', views.product_list),
    path('product_detail/<int:pk>/', views.product_detail),
    path('shift_list/', views.shift_list),
    path('shift_list_detail/<int:pk>/', views.shift_list_detail),
    path('order_list/', views.order_list),
    path('order_list_detail/<int:pk>/', views.order_list_detail),
    path('order_delete/<int:pk>/', views.order_delete),
    path('users_list/', views.users_list),
    path('users_list_detail/<int:pk>/', views.users_list_detail),
    re_path(r'^auth2/', include('djoser.urls.authtoken')),
]