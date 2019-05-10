from rest_framework import viewsets,permissions
from sales.models.transaction_model import Transactions
from sales.serializers.transaction_serializer import TransactionSerializer

"""
    This is Transaction view in root api
"""
class TransactionView(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)