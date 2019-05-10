from sales.models.client_sales_model import ClientSales
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

"""
    This is view renders Client List page with all the clients
"""
class ClientSalesList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'client_sales_list.html'

    def get(self,request):
        queryset = ClientSales.objects.all()
        context = {
            "sales": queryset,
            "title": "All Client Sales"
        }
        return Response(context)