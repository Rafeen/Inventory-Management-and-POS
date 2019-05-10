from sales.models.orders_model import Order
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

"""
    This is view renders Order List page with all the orders
"""
class OrderList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'order_list.html'

    def get(self, request):
        queryset = Order.objects.all()
        context = {
            "orders": queryset,
            "title": "All Orders"
        }
        return Response(context)