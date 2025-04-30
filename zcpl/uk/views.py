from django.shortcuts import render

# Create your views here.
def uk_home(request):
    return render(request,'uk/uk_home.html')

def uk_contact(request):
    return render(request,'uk/contact.html')