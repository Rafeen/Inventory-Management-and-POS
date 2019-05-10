from django.db import models
from django.urls import reverse


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255)
    brand_description = models.TextField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.brand_name

    def get_absolute_url(self):
        return reverse("brand-details",kwargs={"id": self.brand_id})