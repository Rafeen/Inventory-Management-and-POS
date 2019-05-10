from rest_framework_json_api import serializers
from product.models import ReStock



class ReStockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReStock
        fields = ('restock_id', 'sku', 'batch_number', 'restock_price', 'barcode', 'status', 'restocked_at',
                  'restock_updated_at')
