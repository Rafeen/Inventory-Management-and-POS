from django.db import models
from django.urls import reverse
from .product_model import Product


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    sku = models.ForeignKey(Product, on_delete=models.CASCADE)
    batch_number = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_tax = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0, null=False)
    barcode = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=15)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return str(self.sku)

    def get_absolute_url(self):
        return reverse("stock-details", kwargs={"id": self.stock_id})