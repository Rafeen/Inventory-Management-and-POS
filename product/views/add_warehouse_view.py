from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def create_warehouse(request):
    """
    This view Renders Create Category Page
    """
    if not request.user.is_viewer :
        context = {
            "title": "Create Warehouse"
        }
        return render(request, 'add_warehouse.html',context)
    else:
        return redirect('/dashboard/')