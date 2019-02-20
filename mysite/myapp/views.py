from django.shortcuts import render

from django.http import HttpResponse 
# Create your views here.

def index(request):
	mycontext = {
		'data' : 'welcome to my TourGo'

	}
	return render(request, 'myapp/index.html', mycontext)