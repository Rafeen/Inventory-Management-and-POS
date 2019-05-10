from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product.models import Category


@login_required(login_url='/login/')
def create_category(request):
    """
    This view Renders Create Category Page
    """
    category = Category.objects.all()
    if not request.user.is_viewer :
        context = {
            "title": "Create Category",
            "categories" : category

        }
        return render(request, 'add_category.html',context)
    else:
        return redirect('/dashboard/')
