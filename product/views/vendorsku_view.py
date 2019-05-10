from rest_framework import viewsets,permissions
from product.models import VendorSku
from product.serializers import VendorSkuSerializer

"""
    This is Vendor Sku view in root api
"""
class VendorSkuView(viewsets.ModelViewSet):
    queryset = VendorSku.objects.all()
    serializer_class = VendorSkuSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

