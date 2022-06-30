
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name  


class Item(models.Model):
    item = models.CharField(max_length=100)
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.item  

class CustomerOrder(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    item =models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.BigIntegerField()