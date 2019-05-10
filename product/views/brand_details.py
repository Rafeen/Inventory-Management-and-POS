from django.shortcuts import render, redirect, get_object_or_404
from product.models.brand_model import Brand
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def brand_detail_view(request, id):
    """
        This view renders User Detail page with a details of selected user
    """

    brand_obj = get_object_or_404(Brand, brand_id=id)
    context = {
        "brand": brand_obj,
        "title": "Category Details"

    }
    return render(request, "brand_details.html", context)





