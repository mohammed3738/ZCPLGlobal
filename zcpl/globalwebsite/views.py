from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
# Create your views here.
def home(request):
    return render(request,'main/index.html')

def about_us(request):
    return render(request,'main/about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Save to database
        ContactMessageGlobal.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_RECEIVER_EMAIL],
            fail_silently=False,
        )


    return render(request,'main/contact.html')

def services(request):
    return render(request,'services/services.html')


def itadservices(request):
    return render(request,'services/itad_services.html')

def it_hardware(request):
    return render(request,'services/it_hardware.html')

def server_maintenance(request):
    return render(request,'services/server_maintenance.html')

def storage_maintenance(request):
    return render(request,'services/storage_maintenance.html')

def network_maintenance(request):
    return render(request,'services/network_maintenance.html')

def rental_services(request):
    return render(request,'services/rental_services.html')

def infrastructure_service(request):
    return render(request,'services/infrastructure_service.html')

def global_it(request):
    return render(request,'services/global_it.html')

def microsoft_vm(request):
    return render(request,'services/microsoft_vm.html')


def privacy(request):
    return render(request,'main/privacy.html')


def term(request):
    return render(request,'main/terms.html')


