from sales.models.transaction_model import Transactions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

"""
    This is view renders Order List page with all the orders
"""
class TransactionList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'transaction_list.html'

    def get(self,request):
        queryset = Transactions.objects.all()
        context = {
            "transactions": queryset,
            "title": "All Transactions"
        }
        return Response(context)