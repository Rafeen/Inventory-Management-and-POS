from rest_framework_json_api import serializers
from product.models.serial_model import Serial


class SerialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serial
        fields = ('stock_id', 'serial_number')

