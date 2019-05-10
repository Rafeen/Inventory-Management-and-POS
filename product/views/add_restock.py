from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def add_restock(request):
    """
    This view renders Create brand Page    """
    if not request.user.is_viewer :
        context = {
            "title": "Restock Product"
        }
        return render(request, 'add_restock.html',context)
    else:
        return redirect('/dashboard/')
