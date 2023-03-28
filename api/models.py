from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Вы не ввели Email')
        if not username:
            raise ValueError('Вы не ввели Логин')
        email = self.normalize_email(email)
        user = self.model(
            email=self.normalize_email(email), 
            username=username, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username, password):
        return self._create_user(email, username, password)
    
    def create_superuser(self, email, username, password):
        user = self._create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Country(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ManyToManyField(Manufacturer)
    country = models.ManyToManyField(Country)
    is_new = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ManyToManyField(Product)
    def __str__(self):
        return self.user

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    def __str__(self):
        return self.user
