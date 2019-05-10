from django.shortcuts import render, redirect, get_object_or_404
from product.models.warehouse_model import Warehouse
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def warehouse_detail_view(request, id):
    """
        This view renders Warehouse Detail page with a details of selected Warehouse
    """
    warehouse_obj = get_object_or_404(Warehouse, wh_id=id)
    context = {
        "warehouse": warehouse_obj,
        "title": "Warehouse Details"

    }
    return render(request, "warehouse_details.html", context)

