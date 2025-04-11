
from django.urls import path

from globalwebsite import views

urlpatterns = [    
    path('',views.home,name="home"),
    path('about-us',views.about_us,name="about_us"),
    path('services',views.services,name="services"),
    path('itad-services',views.itadservices,name="itad-services"),
    path('it-hardware',views.it_hardware,name="it-hardware"),
    path('server-maintenance',views.server_maintenance,name="server-maintenance"),
    path('storage-maintenance',views.storage_maintenance,name="storage-maintenance"),
    path('network-maintenance',views.network_maintenance,name="network-maintenance"),
    path('rental-services',views.rental_services,name="rental-services"),



]

