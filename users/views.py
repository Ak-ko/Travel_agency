from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import UserFacts

from django.contrib import messages


def register(request):    
    if request.method == 'POST':                
        password = request.POST['password']
        if len(password) == 8:
            username = request.POST['username']            
            email = request.POST['email']

            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Same email')
            else:
                user = User(username=username, password=password, email=email)                

                identity = request.POST['identity']
                phonenumber = request.POST['phonenumber']     

                if UserFacts.objects.filter(identitynumber=identity).exists() or UserFacts.objects.filter(phonenumber=phonenumber):
                    messages.warning(request, 'Same phone or identity')
                else:
                    user_fact = UserFacts(phonenumber=phonenumber, identitynumber=identity, user=user)
                    user_fact.save()
                    user.save()
                
                    return redirect('travel-home')
        else:
            messages.warning(request, 'Password should have 8 characters.')
    else:
        pass
    return render(request, 'users/register.html')

def login(request):
    if request.method == 'POST':
        pass
    else:
        pass
    return render(request, 'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')
        