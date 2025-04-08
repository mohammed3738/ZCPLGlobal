from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'main/index.html')

def about_us(request):
    return render(request,'main/about.html')

def services(request):
    return render(request,'services/services.html')