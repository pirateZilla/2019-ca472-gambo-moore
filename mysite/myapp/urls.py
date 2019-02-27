from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('quote/', views.quote, name="quote"),
    path('user_dash/', views.user_dash, name="user_dash"),  
    path('register/', views.register, name='register')  

 
]