from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('quote/', views.quote, name="quote"),
    path('user_dash/', views.user_dash, name="user_dash"),  
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),  
    path('registration/', views.registration, name='registration'),
    path('maintenance_checklist/', views.maintenance_checklist, name='maintenance_checklist'),
    path('learning_platform/', views.learning_platform, name='learning_platform'),
    path('speed_learn/', views.speed_learn, name='speed_learn'),
    path('smoothness_learn/', views.smoothness_learn, name='smoothness_learn'),
    path('fatigue_learn/', views.fatigue_learn, name='fatigue_learn'),
    path('tod_learn/', views.tod_learn, name='tod_learn')

 
]