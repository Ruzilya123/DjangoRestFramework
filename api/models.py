from django.db import models

class Product(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=200)
    size = models.CharField(verbose_name="Размер", max_length=200)
    manufacturer = models.ForeignKey('Manufacturer', verbose_name="Производитель", on_delete=models.CASCADE)
    category = models.ForeignKey('Category', verbose_name="Категория", on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name="Цена")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    name = models.CharField(verbose_name="Наименование", max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
    
class Manufacturer(models.Model):
    name = models.CharField(verbose_name="Название фирмы", max_length=200)
    country = models.CharField(verbose_name="Страна производитель", max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
