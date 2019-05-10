from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    parent_id = models.IntegerField(null=True)
    category_description = models.TextField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse("category-details",kwargs={"id": self.category_id})

