from django.db import models

# Create your models here.
class Driver(models.Model):

    f_name = models.CharField(max_length=30, blank=True)
    age = models.CharField(max_length=50, blank=True)
    eircode = models.CharField(max_length=50, blank=True)
    drive_exp = models.CharField(max_length=5, blank=True)

    def  __str__(self):
    	return self.name


