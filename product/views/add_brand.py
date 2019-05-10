from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def create_brand(request):
    """
    This view renders Create brand Page    """
    if not request.user.is_viewer :
        context = {
            "title": "Create Brands"
        }
        return render(request, 'add_brand.html',context)
    else:
        return redirect('/dashboard/')
