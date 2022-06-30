from django.urls import path
from . import views

urlpatterns = [


    path('description',views.description,name='description'),
    path('allitems',views.allitems,name='allitems'),
    path('getsingleitem/<int:id>',views.getsingleitem,name='getsingleitem'),
    path('addItem',views.addItem,name='addItem'),
    path('updateitem/<int:id>',views.updateitem,name='updateitem'),
    path('deleteitem/<int:id>',views.deleteitem,name='deleteitem'),


]
