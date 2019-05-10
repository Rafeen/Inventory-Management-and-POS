from django.db import models
from .stock_model import Stock
from .warehouse_model import Warehouse


class ProductLocation(models.Model):
    prodLoc_id = models.AutoField(primary_key=True)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    wh_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.wh_id.wh_name
