from django.shortcuts import render, redirect, get_object_or_404
from sales.models.transaction_model import Transactions
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def transaction_detail_view(request, id):
    """
        This view renders Warehouse Detail page with a details of selected Warehouse
    """
    transaction_obj = get_object_or_404(Transactions, transaction_id=id)
    context = {
        "transaction": transaction_obj,
        "title": "Transaction Details"

    }
    return render(request, "transaction_details.html", context)

