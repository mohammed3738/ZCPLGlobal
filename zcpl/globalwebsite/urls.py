
from django.urls import path

from globalwebsite import views

urlpatterns = [    
    path('',views.home,name="home"),
    path('about-us',views.about_us,name="about_us"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
    path('itad-services',views.itadservices,name="itad-services"),
    path('it-hardware',views.it_hardware,name="it-hardware"),
    path('server-maintenance',views.server_maintenance,name="server-maintenance"),
    path('storage-maintenance',views.storage_maintenance,name="storage-maintenance"),
    path('network-maintenance',views.network_maintenance,name="network-maintenance"),
    path('rental-services',views.rental_services,name="rental-services"),
    path('infrastructure-managed-service',views.infrastructure_service,name="infrastructure-managed-service"),
    path('global-it',views.global_it,name="global-it"),
    path('microsoft-vm',views.microsoft_vm,name="microsoft-vm"),
    # path('uk',views.uk_home,name="uk-home"),
    # path('uae',views.uae_home,name="uae-home"),
    # path('ca',views.canada_home,name="canada-home"),
    # path('in',views.india_home,name="india-home"),



]

