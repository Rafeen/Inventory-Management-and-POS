from product.models.product_model import Product
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

"""
    This is view renders Product list page with all the products
"""
class ProductList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_list.html'

    def get(self, request):
        queryset = Product.objects.all()
        context = {
            "products": queryset,
            "title": "All Products"
        }
        return Response(context)