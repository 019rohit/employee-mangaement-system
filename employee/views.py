from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    return render(request, 'registration.html')

def employeeLogin(request):
    return render(request, 'employeeLogin.html')

def adminLogin(request):
    return render(request, 'adminLogin.html')
