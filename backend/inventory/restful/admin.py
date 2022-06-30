from django.contrib import admin
from .models import Item, Category,CustomerOrder
# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(CustomerOrder)

