import django_filters
from .models import *

class CollectionCat(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = '__all__'