from django.db import models

class Order(models.Model):
    pet = models.ForeignKey('Pets', on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    shipDate = models.DateTimeField()
    complete = models.BooleanField()
    status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pet.name

class OrderStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Pets(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photoUrls = models.CharField(max_length=255)
    pet_type = models.ForeignKey('PetType', on_delete=models.CASCADE)
    status = models.ForeignKey('PetStatus', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PetType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class PetStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
