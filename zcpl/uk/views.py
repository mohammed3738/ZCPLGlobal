from django.shortcuts import render

# Create your views here.
def uk_home(request):
    return render(request,'uk/main/uk_home.html')
