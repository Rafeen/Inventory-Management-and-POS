from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product.models.product_model import Product


@login_required(login_url='/login/')
def add_stock(request):
    """
    This view renders Create brand Page    """
    prod_obj = Product.objects.all()
    if not request.user.is_viewer :
        context = {
            "title": "Create Stock",
            "products": prod_obj
        }
        return render(request, 'add_stock.html',context)
    else:
        return redirect('/dashboard/')
