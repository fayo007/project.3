from django.db import models

from django.db import models

class Service(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()
    
class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    phone = models.CharField(max_length = 13)

class Price(models.Model):
    status = models.CharField(max_length = 255)
    price = models.IntegerField()
    is_active = models.BooleanField()
    
class Product(models.Model):
    title =models.CharField(max_length=255)
    
    
    
    
