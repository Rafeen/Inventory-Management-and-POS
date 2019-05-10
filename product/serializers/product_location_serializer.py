from rest_framework_json_api import serializers
from product.models.product_location_model import ProductLocation


class ProductLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductLocation
        fields = ('stock_id', 'wh_id', 'created_at', 'updated_at')
