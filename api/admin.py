from django.contrib import admin

from .models import Group, Staff, Product, Shift, Order, UserModel

admin.site.register(Group)
admin.site.register(Staff)
admin.site.register(Product)
admin.site.register(Shift)
admin.site.register(Order)
admin.site.register(UserModel)