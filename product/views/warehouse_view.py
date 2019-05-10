from rest_framework import viewsets,permissions
from product.models import Warehouse
from product.serializers import WarehouseSerializer

"""
    This is warehouse view in root api
"""
class WarehouseView(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

