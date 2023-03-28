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
    language = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Excursion(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    cost = models.IntegerField()
    def __str__(self):
        return self.name

class Tour(models.Model):
    name = models.CharField(max_length=255)
    country = models.ManyToManyField(Country)
    time = models.CharField(max_length=255, choices=(
        ('1 week', '1 week'),
        ('2 weeks', '2 weeks'),
        ('3 weeks', '3 weeks'),
    ))
    service = models.CharField(max_length=255, choices=(
        ('all inclusive', 'all inclusive'),
        ('none', 'none'),
    ))
    count = models.IntegerField()
    hotel = models.CharField(max_length=255, choices=(
        ('3 stars', '3 stars'),
        ('4 stars', '4 stars'),
        ('5 stars', '5 stars'),
    ))
    excursion = models.ManyToManyField(Excursion)
    cost = models.IntegerField()
    def __str__(self):
        return self.name

class PersonalCabinet(models.Model):
    tour = models.ManyToManyField(Tour)
    cost = models.IntegerField()
    time = models.CharField(max_length=255)
    def __str__(self):
        return self.tour.name

class Cart(models.Model):
    user = models.ManyToManyField(User)
    tour = models.ManyToManyField(Tour)
    def __str__(self):
        return self.tour.name

