from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyUserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('Вы не ввели Логин')
        user = self.model(
            username=username, 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, password):
        return self._create_user(username, password)
    
    def create_superuser(self, username, password):
        user = self._create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = MyUserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    description = models.CharField(max_length=255)
    photo = models.FileField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Film(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    reviews = models.IntegerField()
    poster = models.FileField()
    date_out = models.DateField()
    country = models.CharField(max_length=255)
    actor = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user = models.ManyToManyField(User)
    text = models.CharField(max_length=255)
    movie = models.ManyToManyField(Film)

    def __str__(self):
        return self.user    


