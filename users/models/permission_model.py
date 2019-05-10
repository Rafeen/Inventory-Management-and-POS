from django.db import models

class Permissions(models.Model):
	#id 	   =
	#module    =
	role_id    = models.IntegerField(max_length=5, blank=False, null=False)
	create 	   = models.BooleanField(default=True, null=False)
	read 	   = models.BooleanField(default=True, null=False)
	update 	   = models.BooleanField(default=True, null=False)
	delete 	   = models.BooleanField(default=True, null=False)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)