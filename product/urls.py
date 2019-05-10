from django.urls import path, include
from . import views
from rest_framework import routers
from .views.brand_list_view import BrandList
from .views.add_brand import create_brand
from .views.add_category import create_category
from .views.category_list_view import CategoryList
from .views.category_details_view import category_detail_view
from .views.add_product_view import create_product
from .views.stock_list_view import StockList
from .views.add_warehouse_view import create_warehouse
from .views.warehouse_list_view import WarehouseList
from .views.products_list_view import ProductList
from .views.add_stock import add_stock
from .views.add_restock import add_restock
from .views.warehouse_detail import warehouse_detail_view
from .views.stock_details import stock_detail_view
from .views.product_details import product_detail_view
from .views.brand_details import brand_detail_view


router = routers.DefaultRouter()
router.register('brand', views.BrandView)
router.register('category', views.CategoryView)
router.register('product', views.ProductView)
router.register('stock', views.StockView)
router.register('restock', views.RestockView)
router.register('warehouse', views.WarehouseView)
router.register('product_location', views.ProductLocationView)
router.register('serial', views.SerialView)
router.register('vendor_sku', views.VendorSkuView)


urlpatterns = [

    path('products/', ProductList.as_view(), name='list_product'),
    path('create-product/', create_product, name='create_product'),
    path('product/<id>/', product_detail_view, name='product-details'),

    path('create-category/', create_category, name='create_category'),
    path('categories/', CategoryList.as_view(), name='list_category'),
    path('category/<int:id>/',category_detail_view , name='category-details'),

    path('brands/', BrandList.as_view(), name='list_brands'),
    path('create-brands/', create_brand, name='create_brands'),
    path('brand/<int:id>/', brand_detail_view, name='brand-details'),

    path('create-warehouse/', create_warehouse, name='add_warehouse'),
    path('warehouses/', WarehouseList.as_view(), name='warehouse_list'),
    path('warehouse/<int:id>/', warehouse_detail_view, name='warehouse-detail'),

    path('create-stock/', add_stock, name='add_stock'),
    path('create-restock/', add_restock, name='add_restock'),
    path('stock-products/', StockList.as_view(), name='list_stock_product'),
    path('stock/<int:id>', stock_detail_view, name='stock-details'),

    # API URLs
    path('api/inventory/', include(router.urls)),
]