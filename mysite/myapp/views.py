from django.shortcuts import render, render_to_response
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render_to_response("index.html")

def quote(request):
	return render_to_response("quote.html")

def user_dash(request):
	return render_to_response("user_dash.html")