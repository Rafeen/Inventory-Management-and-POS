from product.models.brand_model import Brand
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class BrandList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'brand_list.html'

    def get(self,request):
        queryset = Brand.objects.all()
        context = {
            "brands": queryset,
            "title": "All Brands"
        }
        return Response(context)