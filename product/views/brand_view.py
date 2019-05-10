from rest_framework import viewsets,permissions
from product.models import Brand
from product.serializers import BrandSerializer


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

