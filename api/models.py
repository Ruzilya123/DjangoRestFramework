from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fio = models.CharField(max_length=255) # нужное нам поле
    gender = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class Product(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.IntegerField()

class Cart(models.Model):
    product = models.ManyToManyField(Product)

class Order(models.Model):
    product = models.ManyToManyField(Product)
    total_price = models.IntegerField()
