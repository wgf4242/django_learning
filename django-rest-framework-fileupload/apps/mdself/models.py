from django.db import models

# Create your models here.
class Category(models.Model):
    parentCategory = models.ForeignKey('self', blank=True, null=True, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)