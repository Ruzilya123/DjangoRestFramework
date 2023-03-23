from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    isbn = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class OrderedBook(models.Model):
    name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    total_price = models.IntegerField()

    def __str__(self):
        return self.name
