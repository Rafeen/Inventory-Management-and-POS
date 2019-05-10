from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product.models.warehouse_model import Warehouse
from sales.models.client_model import Clients
from product.models.stock_model import Stock

"""
    This is page renders client sales page to add sold product to client 
"""
@login_required(login_url='/login/')
def client_sales(request):
    """
    This view Renders Create Order Page
    """
    warehouse = Warehouse.objects.all()
    clients = Clients.objects.all()
    stocks = Stock.objects.all()
    if not request.user.is_viewer :
        context = {
            "title": "Client Sales",
            "stocks": stocks,
            "warehouses": warehouse,
            "clients": clients,
        }
        return render(request, 'client_sales.html', context)
    else:
        return redirect('/dashboard/')