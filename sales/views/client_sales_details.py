from django.shortcuts import render, redirect, get_object_or_404
from sales.models.client_sales_model import ClientSales
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def client_sales_detail_view(request, id):
    """
        This view renders Warehouse Detail page with a details of selected Warehouse
    """
    sale_obj = get_object_or_404(ClientSales, client_sales_id=id)
    context = {
        "clientSale": sale_obj,
        "title": "Client Sales Details"

    }
    return render(request, "client_sales_details.html", context)

