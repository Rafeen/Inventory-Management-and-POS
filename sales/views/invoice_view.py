from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def invoice_page_view(request):
    """
    This view Renders Create Bundle Page
    """
    if not request.user.is_viewer :
        context = {
            "title": "Invoice"
        }
        return render(request, 'invoice.html', context)
    else:
        return redirect('/dashboard/')
