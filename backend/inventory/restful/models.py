
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token

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




@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)