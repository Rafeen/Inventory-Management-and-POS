from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from sales.models.bundle_product_model import Bundle
from sales.models.bundle_product_model import BundleProducts
from product.models.stock_model import Stock


@login_required(login_url='/login/')
def bundle_products_list(request,id):
    """
    This view Renders Bundle Product list Page    """
    bundle = get_object_or_404(Bundle, bundle_id=id)
    bundleProd = BundleProducts.objects.filter(bundle=id)
    stocks = Stock.objects.all()
    context = {
        "title": "Bundle Products List",
        "bundle": bundle,
        "bundleproducts": bundleProd,
        "stocks": stocks
    }
    return render(request, 'bundle_products.html',context)

