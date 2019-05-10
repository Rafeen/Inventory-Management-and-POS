from django.contrib import admin
from .models import Product
from .models import Category
from .models import Brand
from .models import Stock
from .models import Warehouse
from .models import Serial
from .models import ProductLocation
from .models import ReStock
from .models import VendorSku



# Register your models here.
admin.site.register(Product)
admin.site.register(VendorSku)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Stock)
admin.site.register(ReStock)
admin.site.register(Warehouse)
admin.site.register(Serial)
admin.site.register(ProductLocation)
