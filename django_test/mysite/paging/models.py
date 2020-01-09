from django.db import models

# Create your models here.

class Host(models.Model):
	
	HostName = models.CharField(max_length=20)	

	IP = models.GenericIPAddressField()
