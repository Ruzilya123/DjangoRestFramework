from django.db import models
from django.contrib.auth.models import User

class Class(models.Model):
    class_name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    students = models.ManyToManyField('Student', related_name='students')
    
class Student(models.Model):
    fio = models.CharField(max_length=100)
    age = models.IntegerField()
    subjects = models.ManyToManyField('Subject', related_name='subjects')
    marks = models.CharField(max_length=100, blank=True, choices=(
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ))
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
