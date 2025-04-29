
from django.urls import path

from . import views

urlpatterns = [    

    path('',views.uk_home,name="uk-home"),


]

