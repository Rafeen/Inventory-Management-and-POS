from django.shortcuts import render, redirect, get_object_or_404
from product.models.product_model import Product
from product.models.category_model import Category
from product.models.brand_model import Brand
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def product_detail_view(request, id):
    """
        This view renders User Detail page with a details of selected user
    """

    prod_obj = get_object_or_404(Product, sku=id)
    category = Category.objects.all()
    brand = Brand.objects.all()
    print(prod_obj)
    context = {
        "product": prod_obj,
        "title": "Product Details",
        "categories":category,
        "brands":brand

    }
    return render(request, "products_details.html", context)





