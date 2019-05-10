from sales.models.client_model import Clients
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

"""
    This is view renders Client List page with all the clients
"""
class ClientList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'client_list.html'

    def get(self,request):
        queryset = Clients.objects.all()
        context = {
            "clients": queryset,
            "title": "All Clients"
        }
        return Response(context)