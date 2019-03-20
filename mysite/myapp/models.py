from django.db import models

# Create your models here.
class Driver(models.Model):

    f_name = models.CharField(max_length=20, blank=True)
    l_name = models.CharField(max_length=20, blank=True)
    dob = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)


    #premium = models.IntegerField(max_length=5, blank=True)
    #email = models.EmailField(max_length=50, blank=True)

    def  __str__(self):
    	return self.f_name


class Car(models.Model):
    Driver = models.OneToOneField(Driver, on_delete=models.CASCADE, primary_key=True, )
    car_type = models.CharField(max_length=20, blank=True)
    car_reg = models.CharField(max_length=20, blank=True)
    car_mileage= models.CharField(max_length=20, blank=True)
    engine_size = models.CharField(max_length=50, blank=True)
   


    #premium = models.IntegerField(max_length=5, blank=True)
    #email = models.EmailField(max_length=50, blank=True)

    def  __str__(self):
        return self.car_type




class Maintenance(models.Model):
    Driver = models.OneToOneField(Driver, on_delete=models.CASCADE, primary_key=True, )
    coolent_level = models.CharField(max_length=20, blank=True)
    battery = models.CharField(max_length=20, blank=True)
    oil_level = models.CharField(max_length=20, blank=True)
    windscreen_washer = models.CharField(max_length=20, blank=True)
    break_fluid = models.CharField(max_length=20, blank=True)
    tyre_dept = models.CharField(max_length=20, blank=True)
   


    def  __str__(self):
        return self.coolent_level


class Journeys(models.Model):
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    journey_score = models.CharField(max_length=20, blank=True)
    date = models.CharField(max_length=20, blank=True)
    start_time = models.CharField(max_length=20, blank=True)
    end_time = models.CharField(max_length=20, blank=True)
    distance = models.CharField(max_length=20, blank=True)
    end_location = models.CharField(max_length=20, blank=True)
    end_location = models.CharField(max_length=20, blank=True)
   


    #premium = models.IntegerField(max_length=5, blank=True)
    #email = models.EmailField(max_length=50, blank=True)

    def  __str__(self):
        return self.journey_score
        