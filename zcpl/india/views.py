from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from .models import *
# Create your views here.


def india_home(request):
    return render(request,'india/india_home.html')

# def india_contact(request):
#     return render(request,'india/contact.html')





# def india_contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             phone = form.cleaned_data['phone']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             full_message = f"""
#             Name: {name}
#             Email: {email}
#             Phone: {phone}
#             Subject: {subject}
            
#             Message:
#             {message}
#             """

#             send_mail(
#                 subject=f"Contact Form Submission: {subject}",
#                 message=full_message,
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 recipient_list=[settings.CONTACT_EMAIL],  # Define in settings.py
#                 fail_silently=False,
#             )
#             print('done')
#             # return redirect("contact_success")  # Add a success page
#     else:
#         form = ContactForm()
    
#     # return render(request, "contact.html", {"form": form})
#     return render(request,'india/contact.html',{"form": form})



# def india_contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         # Save to database
#         ContactMessage.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             subject=subject,
#             message=message
#         )

#         full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

#         send_mail(
#             subject,
#             full_message,
#             settings.DEFAULT_FROM_EMAIL,
#             [settings.CONTACT_RECEIVER_EMAIL],
#             fail_silently=False,
#         )

#         return render(request, 'india/contact.html', {'success': True})

#     return render(request, 'india/contact.html')




def india_contact(request): 
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  # ✅ Validate including captcha
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # Save to database
            ContactMessage.objects.create(
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
            request.session['form_submitted'] = True
            return redirect('thank_you')
    else:
        form = ContactForm()

    return render(request, 'india/contact.html', {'form': form, 'success': success})




def india_services(request):
    return render(request, 'india/service.html')

def it_hardware(request):
    return render(request, 'india/it_hardware_in.html')

def server_maintenance_india(request):
    return render(request, 'india/server_maintenance_in.html')

def storage_maintenance_india(request):
    return render(request, 'india/storage_maintenance_in.html')

def network_maintenance_india(request):
    return render(request, 'india/network_maintenance_in.html')

def rental_services_india(request):
    return render(request,'india/rental_services.html')

def email_migration_india(request):
    return render(request,'india/service/email_migration.html')

def infrastructure_service_india(request):
    return render(request,'india/infrastructure_service.html')

def server_mumbai(request):
    return render(request,'india/service/server_mumbai.html')

def server_banglore(request):
    return render(request,'india/service/server_banglore.html')

def server_chennai(request):
    return render(request,'india/service/server_chennai.html')

def server_hyderabad(request):
    return render(request,'india/service/server_hyderabad.html')

def server_ahmedabad(request):
    return render(request,'india/service/server_ahmedabad.html')

def server_kolkata(request):
    return render(request,'india/service/server_kolkata.html')

def server_delhi(request):
    return render(request,'india/service/server_delhi.html')

def server_pune(request):
    return render(request,'india/service/server_pune.html')
