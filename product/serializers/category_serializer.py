from rest_framework_json_api import serializers
from product.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'category_id','category_name', 'parent_id', 'category_description', 'status')
