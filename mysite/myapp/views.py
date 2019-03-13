from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login	
#imports the  driver model so we can save the data to it 
from .models import Driver

# Create your views here.

def index(request):
	return render_to_response("index.html")

def quote(request):
	#remember to validate the data collect first 
	# "firstname" is name="firstname" in the input tag
	f_name = request.GET.get('fname')
	l_name = request.GET.get('lname')
	dob = request.GET.get('bday')
	address = request.GET.get('address_l1')

	print ("jemil is ", f_name, l_name, dob, address )


	
	context={}
	return render(request, "quote.html", context)

def about(request):
	return render_to_response("about.html")

def faq(request):
	return render_to_response("faq.html")

def contact(request):
	return render_to_response("contact.html")

def user_dash(request):
	return render_to_response("user_dash.html")

def registration(request):
	return render_to_response("registration.html")

def login(request):
	return render_to_response("registration/login.html")

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
			return redirect ('index')
	else:
		form = UserCreationForm()

	context = {'form' : form}
	return render(request, "registration/register.html", context)

