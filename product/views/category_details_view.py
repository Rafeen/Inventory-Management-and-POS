from django.shortcuts import render, redirect, get_object_or_404
from product.models.category_model import Category
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def category_detail_view(request, id):
    """
        This view renders User Detail page with a details of selected user
    """

    cat_obj = get_object_or_404(Category, category_id=id)
    context = {
        "category": cat_obj,
        "title": "Category Details"

    }
    return render(request, "category_details.html", context)





