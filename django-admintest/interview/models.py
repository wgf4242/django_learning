from django.db import models


# Create your models here.
JOB_CHOICE = (
    (1, 'C1'),
    (2, 'C2')
)

class Person(models.Model):
    name = models.CharField(max_length=180, null=True, blank=True)
    gender = models.CharField(max_length=180, null=True, blank=True)
    education = models.CharField(max_length=180, null=True, blank=True)
    job = models.CharField(max_length=180, null=True, blank=True, choices=JOB_CHOICE)

    def __str__(self):
        return self.name
