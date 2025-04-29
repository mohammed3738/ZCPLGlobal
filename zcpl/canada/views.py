from django.shortcuts import render

# Create your views here.
def canada_home(request):
    return render(request,'canada/canada_home.html')