from ast import arg
from rest_framework import serializers
from restful.models import Item

class InventorySerializer(serializers.ModelSerializer ):
    class Meta:
        model = Item
        fields = '__all__'