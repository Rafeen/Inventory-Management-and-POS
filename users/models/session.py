from django.db import models

class Session(models.Model):
    session_key_id = models.IntegerField(auto_created=True, primary_key=True, unique=True)
    session_ey     = models.CharField(max_length=40, null=False, unique=True)
    session_data   = models.CharField(max_length=40, null=False)
    expiry_date    = models.DateTimeField()
