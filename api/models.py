from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
    
class Cart(models.Model):
    products = models.ManyToManyField(Product)

    def __str__(self):
        return str(self.products)
    
    def total_price(self):
        return sum(item.price for item in self.products.all())
