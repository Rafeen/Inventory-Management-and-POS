from rest_framework_json_api import serializers
from product.models.vendor_sku import VendorSku


class VendorSkuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendorSku
        fields = ('owner_sku', 'vendor_sku', 'client_name')
