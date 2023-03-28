from django.urls import include, path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tours', views.TourViewSet)
router.register('countries', views.CountryViewSet)
router.register('excursions', views.ExcursionViewSet)
router.register('personals', views.PersonalCabinetViewSet)
router.register('carts', views.CartViewSet)

urlpatterns = [
    path('login/', views.LoginUserView.as_view()),
    path('register/', views.RegistrUserView.as_view()),
    path('logout/', views.LogOutUserView.as_view()),
    path('employee/', views.get_employee),
    path('', include(router.urls)),
]

# Admin email: admin@admin.ru; password: admin, username: admin;
