from django.db import models

# Create your models here.
class Driver(models.Model):

    name = models.CharField(max_length=30, blank=True)
    age = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    experience = models.CharField(max_length=5, blank=True)

    def  __str__(self):
    	return self.name


