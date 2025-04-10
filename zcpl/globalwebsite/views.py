from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'main/index.html')

def about_us(request):
    return render(request,'main/about.html')

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