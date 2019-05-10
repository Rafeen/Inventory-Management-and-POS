from django.db import models
from .orders_model import Order
from product.models.stock_model import Stock


class OrderedProducts(models.Model):
    orderedProd_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Stock, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    quantity = models.IntegerField(blank=False, null=False,default=0)

    def __str__(self):
        return self.orderedProd_id

