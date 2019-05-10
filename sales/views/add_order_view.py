from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product.models.product_model import Product
from sales.models.client_model import Clients

@login_required(login_url='/login/')
def create_order(request):
    """
    This view Renders Create Order Page
    """
    clients = Clients.objects.all()
    products = Product.objects.all()
    if not request.user.is_viewer :
        context = {
            "title": "New Order",
            "products": products,
            "clients": clients,
        }
        return render(request, 'add_order.html',context)
    else:
        return redirect('/dashboard/')