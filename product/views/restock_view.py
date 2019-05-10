from rest_framework import viewsets, permissions
from product.models import ReStock
from product.serializers import ReStockSerializer

"""
    This is Restock view in root api
"""
class RestockView(viewsets.ModelViewSet):
    queryset = ReStock.objects.all()
    serializer_class = ReStockSerializer
