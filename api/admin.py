from django.contrib import admin
from .models import Order, OrderStatus, Pets, Category, PetType, PetStatus

admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(Pets)
admin.site.register(Category)
admin.site.register(PetType)
admin.site.register(PetStatus)
