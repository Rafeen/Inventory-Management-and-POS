from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from sales.models.orders_model import Order

@login_required(login_url='/login/')
def create_transaction(request):
    """
    This view Renders Create Category Page
    """
    orders = Order.objects.all()
    if not request.user.is_viewer :
        context = {
            "title": "Add Transaction",
            "orders": orders
        }
        return render(request, 'transaction.html',context)
    else:
        return redirect('/dashboard/')