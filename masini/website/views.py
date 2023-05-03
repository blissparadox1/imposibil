from django.shortcuts import render

def home(request):
    return render(request, 'home.html' , {})

def list1(request):
    return render(request, 'car-list-fullWidth.html' , {})

def contact(request):
    return render(request, 'contact.html' , {})
