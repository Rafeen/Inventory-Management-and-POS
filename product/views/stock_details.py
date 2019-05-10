from django.shortcuts import render, redirect, get_object_or_404
from product.models.stock_model import Stock
from product.models.product_model import Product
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def stock_detail_view(request, id):
    """
        This view renders Stock Detail page with a details of selected stock
    """
    stock_obj = get_object_or_404(Stock, stock_id=id)
    product = Product.objects.all()
    context = {
        "stock": stock_obj,
        "title": "Stock Details",
        "products":product

    }
    return render(request, "stock_details.html", context)

