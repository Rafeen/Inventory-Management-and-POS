from rest_framework import viewsets,permissions
from sales.models.ordered_products_model import OrderedProducts
from sales.serializers.ordered_products_serializer import OrderProductSerializer

"""
    This is Ordered product view in root api
"""
class OrderProductView(viewsets.ModelViewSet):
    queryset = OrderedProducts.objects.all()
    serializer_class = OrderProductSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)