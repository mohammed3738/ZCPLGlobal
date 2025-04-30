
from django.urls import path

from . import views

urlpatterns = [    

    path('',views.uae_home,name="uae-home"),
    path('contact',views.uae_contact,name="uae-contact"),




]

