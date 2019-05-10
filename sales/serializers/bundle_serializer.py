from rest_framework_json_api import serializers
from sales.models.bundle_model import Bundle


class BundleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bundle
        fields = ('bundle_name', 'bundle_description', 'status', 'created_at',
                  'updated_at')
