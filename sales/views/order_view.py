from rest_framework import viewsets,permissions
from sales.models.orders_model import Order
from sales.serializers.order_serializer import OrderSerializer

"""
    This is Order view in root api
"""
class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)