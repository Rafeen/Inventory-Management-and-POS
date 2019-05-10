from rest_framework_json_api import serializers
from sales.models.transaction_model import Transactions


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transactions
        fields = ('order','paid_amount', 'payment_method', 'transaction_date', 'status',  'created_by', )
