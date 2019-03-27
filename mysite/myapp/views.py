from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login	
#imports the  driver model so we can save the data to it 
from .models import Driver, Car, Maintenance, Journeys, Speed, Fatigue, Smoothness, TimeOfDay

# Create your views here.

def index(request):
	return render_to_response("index.html")

def quote(request):
	#print (request.user)

	context = {}
	
	return render(request, "quote.html", context)

def about(request):
	return render_to_response("about.html")

def faq(request):
	return render_to_response("faq.html")

def contact(request):
	return render_to_response("contact.html")

def user_dash(request):

	#SQL QUERIES for jemil
	average_JS = Driver.objects.raw('''select myapp_driver.id,  ROUND(AVG(journey_score)) AS avg_journey_score
											from myapp_driver
											join myapp_journeys on myapp_driver.id = myapp_journeys.Driver_id
											where f_name = "jemil"; 
											''')# just change "jemil"

	num_journeys_this_week = Journeys.objects.raw('''select myapp_journeys.id, count(myapp_journeys.id) as trips
													from myapp_journeys
													where Driver_id = "1"; 
	 												''')# just chnage the ID
	km_driven = Journeys.objects.raw('''select myapp_journeys.id,  sum(myapp_journeys.distance) AS km_driven
										from myapp_journeys
										where Driver_id = "1";
								 	''') #JUST CHNAGE THE id 
	context = {

	"journey_score": average_JS,
	"num_trips": num_journeys_this_week,
	"km_driven": km_driven
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

