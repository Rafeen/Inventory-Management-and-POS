from django.db import models
from .category_model import Category
from .brand_model import Brand
from django.urls import reverse


class Product(models.Model):
    sku = models.CharField(primary_key=True, max_length=255, unique=True)
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField(blank=True)
    color = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=100, blank=True)
    weight = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=255, blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.sku + '-' + self.product_name)

    def get_absolute_url(self):
        return reverse("product-details", kwargs={"id": self.sku})







