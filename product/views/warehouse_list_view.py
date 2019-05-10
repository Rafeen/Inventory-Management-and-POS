from product.models.warehouse_model import Warehouse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

"""
    This is page renders Warehouse list page with all the warehouses
"""
class WarehouseList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'warehouse_list.html'

    def get(self,request):
        queryset = Warehouse.objects.all()
        context = {
            "warehouses": queryset,
            "title": "All Warehouses"
        }
        return Response(context)
        