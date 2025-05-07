
from django.urls import path

from . import views

urlpatterns = [    
    
    path('',views.india_home,name="india-home"),
    path('contact',views.india_contact,name="india-contact"),
    path('services', views.india_services, name="india-services"),


]

