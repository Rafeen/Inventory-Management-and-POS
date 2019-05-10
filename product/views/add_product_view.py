from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from product.models.category_model import Category
from product.models.brand_model import Brand


@login_required(login_url='/login/')
def create_product(request):
    """
    This view Renders Create Product Page
    """

    categories = Category.objects.all()
    brands = Brand.objects.all()
    if not request.user.is_viewer :
        context = {
            "title": "Add Product",
            "categories": categories,
            "brands": brands
        }
        return render(request, 'add_product.html',context)
    else:
        return redirect('/dashboard/')
