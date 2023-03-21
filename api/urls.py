from django.urls import include, path
from . import views

urlpatterns = [
    path('students/', views.StudentAPIList.as_view()),
    path('students/<int:pk>/', views.StudentAPIDetail.as_view()),
    path('classes/', views.ClassAPIList.as_view()),
    path('classes/<int:pk>/', views.ClassAPIDetail.as_view()),
    path('subjects/', views.SubjectAPIList.as_view()),
    path('subjects/<int:pk>/', views.SubjectAPIDetail.as_view()),
]