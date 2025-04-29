from django.shortcuts import render

# Create your views here.


def india_home(request):
    return render(request,'india/india_home.html')