from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
# from .forms import ContactForm
from django.conf import settings
from .models import *

# Create your views here.
def uk_home(request):
    return render(request,'uk/uk_home.html')

# def uk_contact(request):
#     return render(request,'uk/contact.html')


def uk_contact(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        # phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Save to database
        ContactMessageUk.objects.create(
            name=name,
            email=email,
            # phone=phone,
            subject=subject,
            message=message
        )

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_RECEIVER_EMAIL],
            fail_silently=False,
        )

        return render(request, 'uk/contact.html', {'success': True})

    return render(request, 'uk/contact.html')



