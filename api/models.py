from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    country = models.CharField(max_length=255)
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Producer(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Poster(models.Model):
    date = models.DateField()
    film = models.ForeignKey('Film', on_delete=models.CASCADE)

