
from django.urls import path

from . import views
# from .views import india_contact

urlpatterns = [    
    
    path('',views.india_home,name="india-home"),
    path('contact',views.india_contact,name="india-contact"),
    path('services', views.india_services, name="india-services"),
    # path("contact/success/", TemplateView.as_view(template_name="success.html"), name="contact_success"),


]

