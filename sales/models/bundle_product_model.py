from django.db import models
from .bundle_model import Bundle
from product.models.stock_model import Stock


class BundleProducts(models.Model):
    bundleprod_id       = models.AutoField(primary_key=True)
    bundle				= models.ForeignKey(Bundle, on_delete=models.CASCADE)
    stock		        = models.ForeignKey(Stock, on_delete=models.CASCADE)
    product_quantity    = models.IntegerField(default=2)
    status 				= models.CharField(max_length=10)
    created_at  		= models.DateTimeField(auto_now=True)
    updated_at			= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stock.sku.product_name