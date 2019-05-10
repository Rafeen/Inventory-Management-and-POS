from rest_framework import viewsets, permissions
from product.models import Stock
from product.serializers import StockSerializer

"""
    This is stock view in root api
"""
class StockView(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
