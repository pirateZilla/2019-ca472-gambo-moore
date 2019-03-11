from django.db import models

# Create your models here.
class Driver(models.Model):

    f_name = models.CharField(max_length=20, blank=True)
    l_name = models.CharField(max_length=20, blank=True)
    emp_status = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=40, blank=True)
    DOB = models.CharField(max_length=20, blank=True)
    licence_type = models.CharField(max_length=50, blank=True)
    drive_exp = models.CharField(max_length=5, blank=True)
    NCB = models.CharField(max_length=5, blank=True)

    def  __str__(self):
    	return self.name


