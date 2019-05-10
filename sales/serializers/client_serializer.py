from rest_framework_json_api import serializers
from sales.models.client_model import Clients


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('url', 'client_name', 'client_description', 'client_address', 'client_email', 'client_phone')
