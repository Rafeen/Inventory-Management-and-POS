from django.urls import path, include
from rest_framework import routers

from . import views
from .views.add_bundle_view import add_bundle_page_view
from .views.add_transaction_view import create_transaction
from .views.transaction_list import TransactionList
from .views.add_order_view import create_order
from .views.add_payment_view import create_payment
from .views.bundle_list_view import bundle_list
from .views.bundle_product_list_view import bundle_products_list
from .views.add_client import create_client
from .views.client_sales import client_sales
from .views.client_list import ClientList
from .views.order_list import OrderList
from .views.invoice_view import invoice_page_view
from .views.transaction_details import transaction_detail_view
from .views.client_sales_list import ClientSalesList
from .views.client_sales_details import client_sales_detail_view



router = routers.DefaultRouter()

router.register('bundle', views.BundleView)
router.register('bundleProduct', views.BundleProductView)
router.register('order', views.OrderView)
router.register('orderProduct', views.OrderProductView)
router.register('transaction', views.TransactionView)
router.register('clients', views.ClientsView)
router.register('clientSales', views.ClientSalesView)




urlpatterns = [
    path('create-bundles/', add_bundle_page_view, name='add_bundle'),
    path('bundles/', bundle_list, name='bundle_list'),

    path('bundles/<int:id>', bundle_products_list, name='bundle_product_list'),

    path('create-order/', create_order, name='add_order'),
    path('all-order/', OrderList.as_view(), name='all_order'),

    path('create-transaction/', create_transaction, name='add_transaction'),
    path('all-transaction/', TransactionList.as_view(), name='all_transaction'),
    path('transaction/<int:id>', transaction_detail_view, name='transaction_detail'),

    path('create-payment/', create_payment, name='add_payment'),

    path('create-client/', create_client, name='add_client'),
    path('create-client-sales/', client_sales, name='client-sales'),
    path('all-client-sales/', ClientSalesList.as_view(), name='client_sales_list'),
    path('client-sales/<int:id>', client_sales_detail_view, name='client_sales_detail'),
    path('clients/', ClientList.as_view(), name='client_list'),

    path('invoice/', invoice_page_view, name='invoice'),

    # API URLs
    path('api/sales/', include(router.urls)),

]