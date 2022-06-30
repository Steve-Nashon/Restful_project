from rest_framework.response import Response
from rest_framework.decorators import api_view
from restful.models import Item 
from api.serializers import InventorySerializer


@api_view(['GET'])
def getdt(request):
    items = Item.objects.all()
    serializer = InventorySerializer(items, many = True )
    return Response(serializer.data)

@api_view(['POST']) 
def addItem(request):
    serializer = InventorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)