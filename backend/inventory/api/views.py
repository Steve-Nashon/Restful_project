from rest_framework.response import Response
from rest_framework.decorators import api_view
from restful.models import Item 
from api.serializers import InventorySerializer

endpoint = "localhost/description"

@api_view(['GET'])
def allitems(request):
    items = Item.objects.all()
    serializer = InventorySerializer(items, many = True )
    return Response(serializer.data)


@api_view(['GET'])
def getsingleitem(request, id):
    item = Item.objects.get(id=id)
    serializer = InventorySerializer(item, many = False )
    return Response(serializer.data)

@api_view(['POST']) 
def addItem(request):
    serializer = InventorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST']) 
def updateitem(request, id):
    item = Item.objects.get(id=id)
    serializer = InventorySerializer(instance = item, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE']) 
def deleteitem(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return Response('Item deleted')

@api_view(['GET'])
def description(request):
    api = {
        'Description':{'name': 'inventory Django REST api'},
        'api_urls':{
           'django_urls': {
        'Register customers': 'localhost/tasks/register',
        'Login customers': 'localhost/tasks/login',
        'logout customers': 'localhost/tasks/logout',
        'retrieve items': 'localhost/tasks/',
        'retrieve orders': 'localhost/tasks/orders',
        'retrive categorys': 'localhost/tasks/retrievecategory',
        'add item': 'localhost/tasks/add',
        'add category': 'localhost/tasks/addcategory',
        'update item': 'localhost/tasks/update/<int:id>',
        'update category': 'localhost/tasks/updatecategory/<int:id>',
        'update order': 'localhost/tasks/updateorder/<int:id>',
        'delete item': 'localhost/tasks/delete/<int:id>',
        'delete category': 'localhost/tasks/deletecategory/<int:id>' 
        },'django_rest_urls':{
            'description': 'localhost/description',
            'retrieving all items': 'localhost/allitems',
            'retrieving single item': 'localhost/getsingleitem/<int:id>',
            'Create items': 'localhost/addItem',
            'Updating an item': 'localhost/updateitem/<int:id>',
        }
        
    }
    
    }
    return Response(api)
