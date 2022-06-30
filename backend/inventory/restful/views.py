from ast import Not
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import is_valid_path
from restful.models import Item, Category, CustomerOrder
from restful.forms import ItemForm,CategoryForm,CustomerForm
from .collection import CollectionCat
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add(request):
    form = ItemForm(request.POST or None)
    #all_item = Item.objects.all
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'add.html',{'form':form})

@login_required
def retrieve(request):
    all_items = Item.objects.all
    #all_categories = Category.objects.all
    all_cat = Item.objects.values('category').order_by('category').distinct()
    filt = CollectionCat(request.GET)
    #all_items = filt.qs


    return render(request, 'inventory.html',{'all_items':all_items, 'all_cat':all_cat, 'filt':filt })

@login_required
def update(request, id ):
    item = Item.objects.get(id = id)
    #all_items = Item.objects.values('category').order_by('category').distinct()
    form = ItemForm( instance = item)
    if request.method == "POST":
        form = ItemForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect(retrieve)
    return render(request, 'update.html',{'form':form})
    

@login_required
def delete(request, id):
    item = Item.objects.get(id = id)
    item.delete()
    return redirect(retrieve)

@login_required
def addcategory(request):
    form = CategoryForm(request.POST or None)
    #all_item = Item.objects.all
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'addcategory.html',{'form':form})

@login_required
def retrievecategory(request):
    all_categories = Category.objects.all
    return render(request, 'category.html',{'all_categories':all_categories})

@login_required
def updatecategory(request, id ):
    cat = Category.objects.get(id = id)
    #all_items = Item.objects.values('category').order_by('category').distinct()
    form = CategoryForm( instance = cat)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance = cat)
        if form.is_valid():
            form.save()
            return redirect(retrievecategory)
    return render(request, 'updatecat.html',{'form':form})
    

@login_required
def deletecategory(request, id):
    item = Category.objects.get(id = id)
    item.delete()
    return redirect(retrievecategory)


@login_required
def orders(request):
    all_Orders = CustomerOrder.objects.all
    return render(request, 'orders.html',{'all_Orders':all_Orders})



@login_required
def updateorder(request, id ):
    order = CustomerOrder.objects.get(id = id)
    #all_items = Item.objects.values('category').order_by('category').distinct()
    form = CustomerForm(instance = order)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance = order)
        if form.is_valid():
            form.save()
            return redirect(retrievecategory)
    return render(request, 'updateorder.html',{'form':form})
    