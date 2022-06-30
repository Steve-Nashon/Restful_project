from django.urls import path
from . import views

urlpatterns = [

    path('apiget',views.getdt,name='api'),
    path('apipost',views.addItem,name='api'),


]