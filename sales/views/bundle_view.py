from rest_framework import viewsets,permissions
from sales.models.bundle_model import Bundle
from sales.serializers.bundle_serializer import BundleSerializer


"""
    This is Bundle view in root api
"""
class BundleView(viewsets.ModelViewSet):
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)