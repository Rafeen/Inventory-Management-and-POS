from django.db import models
from .client_model import Clients

class Order(models.Model):
    id =  models.AutoField(primary_key=True)
    order_id = models.CharField(unique=True, blank=False, max_length=255, default='Order Id Not Specified')
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    order_type = models.CharField(max_length=20)
    created_by = models.CharField(max_length=20)
    order_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_id + '-' + self.client.client_name