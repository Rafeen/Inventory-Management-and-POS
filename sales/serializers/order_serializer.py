from rest_framework_json_api import serializers
from sales.models.orders_model import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'client', 'order_type', 'status', 'created_by', 'order_date',  'created_at',
                  'updated_at')
