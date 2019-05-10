from rest_framework_json_api import serializers
from sales.models.client_sales_model import ClientSales


class ClientSalesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClientSales
        fields = ('sku', 'quantity', 'client', 'warehouse', 'sales_date')