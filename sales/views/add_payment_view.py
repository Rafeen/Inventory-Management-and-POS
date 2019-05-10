from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def create_payment(request):
    """
    This view Renders Create Payment Page    """

    context = {
        "title": "Add Payment"
    }
    return render(request, 'payment.html',context)

