from rest_framework import viewsets,permissions
from sales.models.client_model import Clients
from sales.serializers.client_serializer import ClientSerializer

"""
    This is Client view in root api
"""
class ClientsView(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

