from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login	
#imports the  driver model so we can save the data to it 
from .models import Driver, Car, Maintenance, Journeys, Speed, Fatigue, Smoothness, TimeOfDay
import pprint

# Create your views here.

def index(request):
	return render_to_response("index.html")

def quote(request):
	#print (request.user)
	user_id = request.GET.get('user_id')
	#print (user_id)

	km_driven = Journeys.objects.raw('''select myapp_journeys.id,  sum(myapp_journeys.distance) AS km_driven
										from myapp_journeys
										where Driver_id = 1 ;
								 	''',) 

	for x in km_driven:
		print (x.km_driven)
	context = {
	"km_driven": km_driven,
	}
	
	return render(request, "quote.html", context)

def about(request):
	return render_to_response("about.html")

def faq(request):
	return render_to_response("faq.html")

def contact(request):
	return render_to_response("contact.html")

def user_dash(request):

	#collects the driver ID from the dropdown 
	user_id = request.GET.get('user_id')

	#SQL QUERIES for diffent drivers 
	average_JS = Driver.objects.raw('''select myapp_driver.id,  ROUND(AVG(journey_score)) AS avg_journey_score, myapp_driver.f_name, myapp_driver.l_name
											from myapp_driver
											join myapp_journeys on myapp_driver.id = myapp_journeys.Driver_id
											where myapp_driver.id = %s;
											''', [user_id]) 

	num_journeys_this_week = Journeys.objects.raw('''select myapp_journeys.id, count(myapp_journeys.id) as trips
													from myapp_journeys
													where Driver_id = %s; 
	 												''', [user_id]) 
	km_driven = Journeys.objects.raw('''select myapp_journeys.id,  sum(myapp_journeys.distance) AS km_driven
										from myapp_journeys
										where Driver_id = %s;
								 	''', [user_id])

	avg_smoothness = Smoothness.objects.raw('''select myapp_journeys.id, Round (avg(myapp_smoothness.Smoothness_level)) AS avg_smoothness, 
												myapp_car.car_type,  myapp_car.car_mileage, myapp_car.car_reg, myapp_car.engine_size
												from myapp_car inner join myapp_journeys on myapp_car.Driver_id = myapp_journeys.Driver_id
												inner join myapp_smoothness on
 												myapp_smoothness.Journeys_id = myapp_journeys.id
												where myapp_car.Driver_id = %s;
											''', [user_id]) 

	avg_fatigue = Fatigue.objects.raw('''select myapp_journeys.id,  Round (avg(myapp_fatigue.fatigue_level)) AS avg_fatigue
										from myapp_car inner join myapp_journeys on myapp_car.Driver_id = myapp_journeys.Driver_id
										inner join myapp_fatigue on
 										myapp_fatigue.Journeys_id = myapp_journeys.id
										where myapp_car.Driver_id = %s;
									 ''', [user_id]) 

	avg_speed = Speed.objects.raw('''select myapp_journeys.id,  Round (avg(myapp_speed.speed_level)) AS avg_speed
									from myapp_car inner join myapp_journeys on myapp_car.Driver_id = myapp_journeys.Driver_id
									inner join myapp_speed on
 									myapp_speed.Journeys_id = myapp_journeys.id
									where myapp_car.Driver_id = %s;
	 							''', [user_id]) 

	TimeOfDay_level= TimeOfDay.objects.raw('''select myapp_journeys.id, Round (avg(myapp_timeofday.time_of_day_level)) AS avg_timeofday
											from myapp_car inner join myapp_journeys on myapp_car.Driver_id = myapp_journeys.Driver_id
											inner join myapp_timeofday on
 											myapp_timeofday.Journeys_id = myapp_journeys.id
											where myapp_car.Driver_id = %s;
	 									''', [user_id]) 

	#test 
	for x in avg_smoothness:
		print (x.avg_timeofday)
	#send to the templte
	#print (km_driven[0])
	context = {

	"journey_score": average_JS,
	"num_trips": num_journeys_this_week,
	"km_driven": km_driven,
	"smoothness": avg_smoothness ,
	"fatigue": avg_fatigue ,
	"speed": avg_speed ,
	"TimeOfDay": TimeOfDay_level,

	}
	return render_to_response("user_dash.html", context)

def registration(request):
	driver = Driver()


	f_name = request.GET.get('fname')
	l_name = request.GET.get('lname')
	dob = request.GET.get('bday')
	address1 = request.GET.get('address_l1')
	address2 = request.GET.get('address_l2')
	print ("the quote details are", f_name, l_name, dob, address1, address2 )
	#sends input data to the model
	"""
	driver.f_name = f_name
	driver.l_name = l_name
	driver.address1 = address1
	driver.address2 = address2
	driver.save()
	"""
	#print(f_name, eircode, drive_exp)

	context={}
	return render(request, "registration.html", context)



def  register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		#checks if data passed to the form is valid 
		if form.is_valid():
			form.save() #saves info to the DB --> creating a new user
			username = form.cleaned_data['username'] #get data passed from the form
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password) #authenticate is a hash funtion in djnago 
			login(request,user)
			return redirect ('login')
	else:
		form = UserCreationForm()

	context = {'form' : form}
	return render(request, "registration/register.html", context)

def login(request, user):

	context = {}
	return redirect ('quote', context)


def maintenance_checklist(request):
	maintenance = Maintenance()


	oil_level = request.GET.get('oil_level')
	battery_level= request.GET.get('battery_level')
	coolent_level = request.GET.get('coolent_level')
	tyre_depth = request.GET.get('tyre_depth')
	windscreen_washer_level = request.GET.get('windscreen_washer_level')
	print ("the maintenance results are", oil_level, battery_level, coolent_level, tyre_depth, windscreen_washer_level)
	#sends input data to the model
	"""
	driver.f_name = f_name
	driver.l_name = l_name
	driver.address1 = address1
	driver.address2 = address2
	driver.save()
	"""
	#print(f_name, eircode, drive_exp)


	return render( request, "maintenance_checklist.html")

def learning_platform(request):


	return render(request, "learning_platform.html")
