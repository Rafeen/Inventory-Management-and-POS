from rest_framework import viewsets,permissions
from product.models import ProductLocation
from product.serializers import ProductLocationSerializer


class ProductLocationView(viewsets.ModelViewSet):
    queryset = ProductLocation.objects.all()
    serializer_class = ProductLocationSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

