from rest_framework_json_api import serializers
from product.models import Stock



class StockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stock
        fields = ('url' ,'stock_id', 'sku', 'stock_quantity','batch_number', 'purchase_price', 'purchase_tax', 'barcode', 'status', 'created_at',
                  'updated_at')
