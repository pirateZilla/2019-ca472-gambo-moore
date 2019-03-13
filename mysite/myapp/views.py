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
	if request.method == "POST":

		#added this line here to save data to the model
		driver = Driver()
		###

		f_name = request.POST.get("fname")
		l_name = request.POST.get("lname")
		emp_status = request.POST.get("drive_exp")
		address = request.POST.get("aLine1")
		DOB = request.POST.get("bday")
		licence_type = request.POST.get("licence")
		NCB = request.POST.get("ncb")
		print(f_name, l_nam, emp_status, address, DOB, licence_type, NCB)
		#sends input data to the model
		#driver.f_name = f_name
		#driver.eircode = eircode
		#driver.drive_exp = drive_exp
		#driver.save()
		#print(f_name, eircode, drive_exp)
		#where do we want to send the user after they submit?
		#return redirect("/myapp/index/")
	
	return render_to_response("quote.html")

def about(request):
	return render_to_response("about.html")

def faq(request):
	return render_to_response("faq.html")

def contact(request):
	return render_to_response("contact.html")

def user_dash(request):
	return render_to_response("user_dash.html")

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

