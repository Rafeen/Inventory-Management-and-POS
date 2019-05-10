from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def create_client(request):
    """
    This view Renders Create Order Page
    """
    if not request.user.is_viewer :
        context = {
            "title": "New Client"
        }
        return render(request, 'add_client.html',context)
    else:
        return redirect('/dashboard/')