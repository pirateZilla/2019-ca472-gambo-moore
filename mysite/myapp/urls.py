from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('quote/', views.quote, name="quote"),
    path('user_dash/', views.user_dash, name="user_dash"),  
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),  
    path('registration/', views.registration, name='registration')

 
]