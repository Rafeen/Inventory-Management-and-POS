from rest_framework_json_api import serializers
from product.models import Warehouse


class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('wh_name', 'wh_address', 'wh_city', 'wh_country', 'wh_phone', 'wh_status', 'wh_type')
