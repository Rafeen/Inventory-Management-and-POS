from rest_framework_json_api import serializers
from product.models import Brand


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('brand_id', 'brand_name', 'brand_description', 'status')
