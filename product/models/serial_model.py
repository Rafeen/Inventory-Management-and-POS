from django.db import models
from .stock_model import Stock

class Serial(models.Model):
    serial_id = models.AutoField(primary_key=True)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.serial_number
