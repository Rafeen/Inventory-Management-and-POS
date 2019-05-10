from rest_framework_json_api import serializers
from sales.models.ordered_products_model import OrderedProducts


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderedProducts
        fields = ('order_id', 'product','quantity', 'status')