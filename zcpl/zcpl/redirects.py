from django.urls import re_path
from django.views.generic.base import RedirectView

redirect_urlpatterns = [
    # Refurbished server redirects
    re_path(r'^refurbished-servers-ahmedabad/?$', RedirectView.as_view(url='/in/refurbished-servers-ahmedabad', permanent=True)),
    re_path(r'^refurbished-servers-banglore/?$', RedirectView.as_view(url='/in/refurbished-servers-banglore', permanent=True)),
    re_path(r'^refurbished-servers-chennai/?$', RedirectView.as_view(url='/in/refurbished-servers-chennai', permanent=True)),
    re_path(r'^refurbished-servers-delhi/?$', RedirectView.as_view(url='/in/refurbished-servers-delhi', permanent=True)),
    re_path(r'^refurbished-servers-hyderabad/?$', RedirectView.as_view(url='/in/refurbished-servers-hyderabad', permanent=True)),
    re_path(r'^refurbished-servers-kolkata/?$', RedirectView.as_view(url='/in/refurbished-servers-kolkata', permanent=True)),
    re_path(r'^refurbished-servers-mumbai/?$', RedirectView.as_view(url='/in/refurbished-servers-mumbai', permanent=True)),
    re_path(r'^refurbished-servers-pune/?$', RedirectView.as_view(url='/in/refurbished-servers-pune', permanent=True)),

    # Other redirects
    re_path(r'^request-quote/?$', RedirectView.as_view(url='/contact-us/', permanent=True)),
]
