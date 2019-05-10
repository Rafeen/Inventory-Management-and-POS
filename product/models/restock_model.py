from django.db import models
from .product_model import Product


class ReStock(models.Model):
    restock_id = models.AutoField(primary_key=True)
    sku = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=255)
    restock_price = models.DecimalField(max_digits=10, decimal_places=2)
    # purchase_tax = models.DecimalField(max_digits=10, decimal_places=2)
    barcode = models.CharField(max_length=255)
    status = models.CharField(max_length=15)
    restocked_at = models.DateField(auto_now=True)
    restock_updated_at = models.DateField(auto_now=True)