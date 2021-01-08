from django.db import models

# Create your models here.


class Product(models.Model):
    serial_number = models.IntegerField(unique=True)
    name = models.TextField()
