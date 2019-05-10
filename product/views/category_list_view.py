from product.models.category_model import Category
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'category_list.html'

    def get(self,request):
        queryset = Category.objects.all()
        context = {
            "categories": queryset,
            "title": "All Categories"
        }
        return Response(context)