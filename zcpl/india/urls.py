
from django.urls import path

from . import views
# from .views import india_contact

urlpatterns = [    
    
    path('',views.india_home,name="india-home"),
    path('contact',views.india_contact,name="india-contact"),
    path('services', views.india_services, name="india-services"),
    path('it-hardware', views.it_hardware, name="it-hardware"),
    path('server-maintenance', views.server_maintenance_india, name="server-maintenance"),
    path('storage-maintenance', views.storage_maintenance_india, name="storage-maintenance"),
    path('network-maintenance', views.network_maintenance_india, name="network-maintenance"),
    # path("contact/success/", TemplateView.as_view(template_name="success.html"), name="contact_success"),


]

