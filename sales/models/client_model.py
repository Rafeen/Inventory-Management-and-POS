from django.db import models
from django.urls import reverse

class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=20, blank=False, null=False)
    client_description = models.CharField(max_length=255)
    client_email = models.EmailField(blank=True, null=True)
    client_phone = models.CharField(max_length=30, blank=True, null=False, default="No Phone Number")
    client_address = models.CharField(max_length=200 , blank=True, null=False, default="No Address")

    def __str__(self):
        return self.client_name

    # def get_absolute_url(self):
    #     return reverse("client-detail", kwargs={"id": self.cleint_id})