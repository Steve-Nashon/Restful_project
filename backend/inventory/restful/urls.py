from django.urls import path
from restful import views

urlpatterns = [

    path('add',views.add,name='add'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('',views.retrieve,name='retrieve'),
    path('orders',views.orders,name='orders'),
    path('updateorder/<int:id>',views.updateorder,name='updateorder'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('retrievecategory',views.retrievecategory,name='retrievecategory'),
    path('updatecategory/<int:id>',views.updatecategory,name='updatecategory'),
    path('deletecategory/<int:id>',views.deletecategory,name='deletecategory'),

]
