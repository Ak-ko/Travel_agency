from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterationForm, UserFactForm
from django.contrib import messages


def register(request):    
    if request.method == 'POST':
        form1 = RegisterationForm(request.POST)
        form2 = UserFactForm(request.POST)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get("username")
            
            messages.success(request, f'Your account with username : {username} is created Successfully')

            return redirect('travel-home')
    else:
        form1 = RegisterationForm()
        form2 = UserFactForm()

    context = {
        "form1" : form1,
        "form2" : form2
    }
    return render(request, 'users/register.html', context)