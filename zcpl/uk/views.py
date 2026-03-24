from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
# from .forms import ContactForm
from django.conf import settings
from .models import *
from .forms import ContactForm
# Create your views here.
def uk_home(request):
    return render(request,'uk/uk_home.html')

def uk_it_hardware(request):
    return render(request,'uk/uk_it_hardware.html')

def uk_server(request):
    return render(request,'uk/uk_server.html')

def uk_server_hdd_sdd(request):
    return render(request,'uk/uk_server_hdd_sdd.html')

def uk_networking(request):
    return render(request,'uk/uk_networking.html')

def uk_server_storage(request):
    return render(request,'uk/uk_server_storage.html')

def uk_server_component(request):
    return render(request,'uk/uk_server_component.html')

def uk_main_service(request):
    return render(request,'uk/uk_main_service.html')

def uk_vmware_support(request):
    return render(request,'uk/uk_vmware_support.html')

def uk_microsoft_support(request):
    return render(request,'uk/uk_microsoft_support.html')

# def uk_contact(request):
#     return render(request,'uk/contact.html')


# def uk_contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         name = request.POST.get('username')
#         email = request.POST.get('email')
#         # phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         # Save to database
#         ContactMessageUk.objects.create(
#             name=name,
#             email=email,
#             # phone=phone,
#             subject=subject,
#             message=message
#         )

#         full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

#         send_mail(
#             subject,
#             full_message,
#             settings.DEFAULT_FROM_EMAIL,
#             [settings.CONTACT_RECEIVER_EMAIL],
#             fail_silently=False,
#         )
#     else:
#         form = ContactForm()

#         return render(request, 'uk/contact.html', {'form':form,'success': True})

#     return render(request, 'uk/contact.html')



def uk_contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  # ✅ Validate including captcha
            name = request.POST.get('name')
            email = request.POST.get('email')
            # phone = form.cleaned_data.get('phone')
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
            request.session['form_submitted'] = True
            return redirect('thank_you')
    else:
        form = ContactForm()

    return render(request, 'uk/contact.html', {'form': form, 'success': success})
