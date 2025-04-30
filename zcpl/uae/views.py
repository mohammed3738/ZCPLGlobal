from django.shortcuts import render



def uae_home(request):
    return render(request,'uae/uae_home.html')


def uae_contact(request):
    return render(request,'uae/contact.html')