from product.models.stock_model import Stock
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

"""
    This view renders Stock List page with all the stocks
"""
class StockList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'stock_list.html'

    def get(self,request):
        queryset = Stock.objects.all()
        context = {
            "stocks": queryset,
            "title": "All Stocks"
        }
        return Response(context)