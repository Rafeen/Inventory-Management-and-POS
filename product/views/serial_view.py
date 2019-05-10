from rest_framework import viewsets,permissions
from product.models import Serial
from product.serializers import SerialSerializer

"""
    This is serial view in root api
"""
class SerialView(viewsets.ModelViewSet):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)

