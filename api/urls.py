from django.urls import include, path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('orderedbooks/', views.OrderedBookList.as_view()),
    path('orderedbooks/<int:pk>/', views.OrderedBookDetail.as_view()),
]