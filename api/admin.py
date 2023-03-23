from django.contrib import admin
from .models import Book, OrderedBook

admin.site.register(Book)
admin.site.register(OrderedBook)