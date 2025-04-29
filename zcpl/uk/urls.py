
from django.urls import path

from . import views

urlpatterns = [    

    path('uk',views.uk_home,name="uk-home"),


]

