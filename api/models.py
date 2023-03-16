from django.db import models

class Order(models.Model):
    table = models.CharField(max_length=100)
    worker = models.ManyToManyField('Workers')
    order_start_time = models.DateTimeField(auto_now_add=True)
    STATUSES = (
        ('new', 'Добавлен'),
        ('in_progress', 'Готовится'),
        ('ready', 'Готов'),
        ('served', 'Оплачен'),
        ('canceled', 'Отменен'),
    )
    status = models.CharField(max_length=100, choices=STATUSES, default='new')
    price = models.IntegerField()

    def __str__(self):
        return self.table
    
    class Meta:
        db_table = 'order'

class Workers(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    position = models.ManyToManyField('Position')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'workers'

class Position(models.Model):
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.position
    
    class Meta:
        db_table = 'position'