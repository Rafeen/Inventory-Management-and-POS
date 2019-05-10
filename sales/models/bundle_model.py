from django.db import models
from django.urls import reverse



class Bundle(models.Model):
    bundle_id          = models.AutoField(primary_key=True)
    bundle_name 	   = models.CharField(max_length=20,blank=False)
    bundle_description = models.TextField()
    status 			   = models.CharField(max_length=10)
    created_at         = models.DateTimeField(auto_now=True)
    updated_at         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bundle_name

    def get_absolute_url(self):
        return reverse("bundle_product_list", kwargs={"id": self.bundle_id})