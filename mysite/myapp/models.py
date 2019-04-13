from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.
class Driver(models.Model):

    f_name = models.CharField(max_length=20, blank=True)
    l_name = models.CharField(max_length=20, blank=True)
    dob = models.PositiveIntegerField( blank=True)
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
    car_mileage= models.PositiveIntegerField( blank=True)
    engine_size = models.PositiveIntegerField( blank=True)
   


    #premium = models.IntegerField(max_length=5, blank=True)
    #email = models.EmailField(max_length=50, blank=True)

    def  __str__(self):
        return self.car_type




class Maintenance(models.Model):
    Driver = models.OneToOneField(Driver, on_delete=models.CASCADE, primary_key=True, )
    coolent_level = models.PositiveIntegerField( blank=True)
    battery = models.PositiveIntegerField( blank=True)
    oil_level = models.PositiveIntegerField( blank=True)
    windscreen_washer = models.PositiveIntegerField( blank=True)
    break_fluid = models.PositiveIntegerField( blank=True)
    tyre_dept = models.PositiveIntegerField( blank=True)
   


    def  __str__(self):
        return self.coolent_level


class Journeys(models.Model):
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    journey_score = models.CharField(max_length=20, blank=True)
    date = models.DateField(default=date.today)
    start_time = models.CharField(max_length=20, blank=True)
    end_time = models.CharField(max_length=20, blank=True)
    distance = models.PositiveIntegerField( blank=True)
    start_location = models.CharField(max_length=20, blank=True)
    end_location = models.CharField(max_length=20, blank=True)
   


    #premium = models.IntegerField(max_length=5, blank=True)
    #email = models.EmailField(max_length=50, blank=True)

    def  __str__(self):
        return self.journey_score
        

class Speed(models.Model):
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    speed_level = models.PositiveIntegerField( blank=True)
    def  __str__(self):
        return self.speed_level



class Fatigue(models.Model):
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    fatigue_level = models.PositiveIntegerField( blank=True)
    def  __str__(self):
        return self.fatigue_level


class TimeOfDay(models.Model):
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    time_of_day_level = models.PositiveIntegerField( blank=True)
    def  __str__(self):
        return self.time_of_day_level


class Smoothness(models.Model):
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    Smoothness_level = models.PositiveIntegerField( blank=True)
    def  __str__(self):
        return self.Smoothness_level


class Month_journey(models.Model):
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    month =  models.CharField(max_length=20, blank=True)
    monthly_journey_score =  models.PositiveIntegerField( blank=True)
    def  __str__(self):
        return self.month
class Real_user(models.Model):

  time=  models.CharField(max_length=20, blank=True)
  lat =  models.CharField(max_length=20, blank=True)
  lon =  models.CharField(max_length=20, blank=True)
  elevation =  models.CharField(max_length=20, blank=True)
  accuracy =  models.CharField(max_length=20, blank=True)
  bearing =  models.CharField(max_length=20, blank=True)
  speed =  models.CharField(max_length=20, blank=True)
  satellites =  models.CharField(max_length=20, blank=True)
  provider =  models.CharField(max_length=20, blank=True)
  hdop =  models.CharField(max_length=20, blank=True)
  vdop = models.CharField(max_length=20, blank=True)
  pdop = models.CharField(max_length=20, blank=True)
  geoidheight = models.CharField(max_length=20, blank=True)
  ageofdgpsdata =  models.CharField(max_length=20, blank=True)
  dgpsid =  models.CharField(max_length=20, blank=True)
  activity =  models.CharField(max_length=20, blank=True)
  battery =  models.CharField(max_length=20, blank=True)
  annotation =  models.CharField(max_length=20, blank=True)
  def  __str__(self):
     return self.time

        