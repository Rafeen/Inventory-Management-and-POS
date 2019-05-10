from django.db import models
from .product_model import Product
from sales.models.client_model import Clients

class VendorSku(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    owner_sku = models.ForeignKey(Product, on_delete=models.CASCADE)
    vendor_sku = models.CharField(max_length=20, blank=True, null=True)
    client_name = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __str__(self):
        return self.vendor_sku