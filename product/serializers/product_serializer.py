from rest_framework_json_api import serializers
from product.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'url', 'sku', 'product_name', 'category', 'brand', 'price', 'tax', 'product_description', 'color', 'size',
            'weight', 'image', 'comment', 'created_at', 'updated_at')
