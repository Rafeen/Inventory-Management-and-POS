from django.db import models
from django.urls import reverse



class Warehouse(models.Model):
    wh_id = models.AutoField(primary_key=True)
    wh_name = models.CharField(max_length=50)
    wh_address = models.TextField()
    wh_city = models.CharField(max_length=20)
    wh_country = models.CharField(max_length=20)
    wh_phone = models.CharField(max_length=20)
    wh_status = models.CharField(max_length=20)
    wh_type = models.CharField(max_length=20)

    def __str__(self):
        return self.wh_name

    def get_absolute_url(self):
        return reverse("warehouse-detail", kwargs={"id": self.wh_id})
