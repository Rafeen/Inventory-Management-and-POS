from rest_framework_json_api import serializers
from sales.models.bundle_product_model import BundleProducts


class BundleProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BundleProducts
        fields = ('bundle', 'stock', 'status', 'created_at',
                  'updated_at')
