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



def india_contact(request):
    if request.method == 'POST':
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

        return render(request, 'india/contact.html', {'success': True})

    return render(request, 'india/contact.html')


def india_services(request):
    return render(request, 'india/service.html')