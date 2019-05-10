from django.contrib import admin
from .models.orders_model import Order
from .models.ordered_products_model import OrderedProducts
from .models.bundle_product_model import BundleProducts
from .models.bundle_model import Bundle
from .models.transaction_model import Transactions
from .models.client_model import Clients
from .models.client_sales_model import ClientSales

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderedProducts)
admin.site.register(Bundle)
admin.site.register(BundleProducts)
admin.site.register(Transactions)
admin.site.register(Clients)
admin.site.register(ClientSales)
