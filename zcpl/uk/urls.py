
from django.urls import path

from . import views

urlpatterns = [    

    path('',views.uk_home,name="uk-home"),    
    path('contact',views.uk_contact,name="uk-contact"),


]

