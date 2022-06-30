from random import choices
from django import forms
from restful.models import Item, Category, CustomerOrder

#choices = [('cat1', 'cat1'), ('cat2', 'cat2'), ('cat3', 'cat3')]
choices = Category.objects.all().values_list('name','name')

choice_list =[]

for c in choices:
    choice_list.append(c)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        #fields = ["item", "category"]
        fields = ("item", "category" )

        widgets = {
            'item' : forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choice_list , attrs ={'class': 'form-select'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        #fields = ["item", "category"]
        fields = ('name',)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerOrder
        fields = '__all__'
    