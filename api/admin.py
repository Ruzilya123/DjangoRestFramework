from django.contrib import admin
from .models import User, Country, Manufacturer, Product, Cart, Order

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
