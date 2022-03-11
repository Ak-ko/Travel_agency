from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterationForm
from django.contrib import messages

def register(request):    
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            
            messages.success(request, f'Your account with username : {username} is created Successfully')
            return redirect('travel-home')
    else:
        form = RegisterationForm()
    return render(request, 'users/register.html', {"form" : form})
