from rest_framework import viewsets, permissions
from product.models import Category
from product.serializers import CategorySerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)
