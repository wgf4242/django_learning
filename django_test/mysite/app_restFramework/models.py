
from django.db import models


class User(models.Model):
	username = models.CharField(max_length=100)
	
class Book(models.Model):
	name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	publisher = models.CharField(max_length=100)
	time = models.CharField(max_length=100)
	owner = models.ManyToManyField(User, related_name='books')
	
