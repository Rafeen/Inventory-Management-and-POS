from django.db import models
from django.urls import reverse

from product.models import Stock
from product.models import Warehouse
from .client_model import Clients

class ClientSales(models.Model):
    client_sales_id = models.AutoField(primary_key=True)
    sku = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, blank=True, null=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, blank=True, null=True)
    sales_date = models.DateField()

    def __str__(self):
        return self.client.client_name + self.warehouse.wh_name

    def get_absolute_url(self):
        return reverse("client_sales_detail", kwargs={"id": self.client_sales_id})
