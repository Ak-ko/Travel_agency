from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    return render(request, 'travel/home.html', {"title" : "Home"})

def login(request):
    return render(request, 'travel/login.html', {"title" : "Login"})

def register(request):
    return render(request, 'travel/register.html', {"title" : "Register"})
