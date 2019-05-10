from rest_framework import viewsets,permissions
from sales.models.client_sales_model import ClientSales
from sales.serializers.client_sales_serializer import ClientSalesSerializer

"""
    This is Client sales view in root api
"""
class ClientSalesView(viewsets.ModelViewSet):
    queryset = ClientSales.objects.all()
    serializer_class = ClientSalesSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

