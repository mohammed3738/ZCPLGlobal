
from django.urls import path

from . import views

urlpatterns = [    

    path('',views.uk_home,name="uk-home"),    
    path('contact',views.uk_contact,name="uk-contact"),
    path('it-hardware',views.uk_it_hardware,name="uk-it-hardware"),
    path('servers/',views.uk_server,name="uk-server"),
    path('server-hard-drives-ssds/',views.uk_server_hdd_sdd,name="uk-server-hdd-sdd"),
    path('enterprise-networking/',views.uk_networking,name="uk-networking"),
    path('server-storage/',views.uk_server_storage,name="uk-server-storage"),
    path('server-components/',views.uk_server_component,name="uk-server-components"),


]

