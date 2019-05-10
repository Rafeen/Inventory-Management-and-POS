from django.db import models
from django.urls import reverse
from .orders_model import Order

class Transactions(models.Model):
    transaction_id  = models.AutoField(primary_key=True)
    order           = models.ForeignKey(Order, on_delete=models.CASCADE)
    paid_amount     = models.FloatField(blank=False, null=False)
    payment_method  = models.CharField(max_length=20)
    transaction_date= models.DateField()
    status          = models.CharField(max_length=20)
    created_by      = models.CharField(max_length=50)
    updated_by      = models.CharField(max_length=50)
    created_at      = models.DateTimeField(auto_now=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order

    def get_absolute_url(self):
        return reverse("transaction-detail", kwargs={"id": self.transaction_id})
