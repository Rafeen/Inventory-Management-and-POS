from rest_framework import viewsets,permissions
from sales.models.bundle_product_model import BundleProducts
from sales.serializers.bundle_product_serializer import BundleProductSerializer

"""
    This is Bundle Product view in root api
"""
class BundleProductView(viewsets.ModelViewSet):
    queryset = BundleProducts.objects.all()
    serializer_class = BundleProductSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)