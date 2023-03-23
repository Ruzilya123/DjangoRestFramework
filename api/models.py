from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100, choices=(
        ('admin', 'admin'),
        ('cook', 'cook'),
        ('waiter', 'waiter'),
    ))

class Staff(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=(
        ('work', 'work'),
        ('not work', 'not work'),
    ))
    group = models.ManyToManyField(Group)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class Shift(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    product = models.ManyToManyField(Product)
    group = models.ManyToManyField(Group)
    staff = models.ManyToManyField(Staff)
    
class Order(models.Model):
    table = models.IntegerField()
    staff = models.ManyToManyField(Staff)
    time = models.DateTimeField()
    status = models.CharField(max_length=100, choices=(
        # принят
        ('accepted', 'accepted'),
        # готовится
        ('cooking', 'cooking'),
        # готов
        ('ready', 'ready'),
        # отменен
        ('canceled', 'canceled'),
        # оплачен
        ('paid', 'paid'),
    ))
    position = models.ManyToManyField(Product)
    price = models.IntegerField()

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    group = models.ManyToManyField(Group)