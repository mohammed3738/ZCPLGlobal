from django.shortcuts import render

# Create your views here.


def india_home(request):
    return render(request,'india/india_home.html')

def india_contact(request):
    return render(request,'india/contact.html')

def india_services(request):
    return render(request, 'india/service.html')