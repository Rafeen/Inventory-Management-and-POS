from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def add_bundle_page_view(request):
    """
    This view Renders Create Bundle Page
    """
    if not request.user.is_viewer :
        context = {
            "title": "Create Bundle"
        }
        return render(request, 'add_bundle.html',context)
    else:
        return redirect('/dashboard/')
