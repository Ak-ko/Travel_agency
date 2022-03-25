from tabnanny import check
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from users.models import UserFacts

from django.contrib import messages

#for checking password 
# from django.contrib.auth.hashers import check_password

def register(request):    
    if request.method == 'POST':                
        password = request.POST['password']
        if len(password) == 8:
            username = request.POST['username']            
            email = request.POST['email']

            if User.objects.filter(email=email).exists() and User.objects.filter(username=username).exists():
                messages.warning(request, 'Same email or Same username')
            else:
                user = User(username=username, password=password, email=email)                                
            
                identity = request.POST['identity']
                phonenumber = request.POST['phonenumber']     

                if UserFacts.objects.filter(identitynumber=identity).exists() or UserFacts.objects.filter(phonenumber=phonenumber):
                    messages.warning(request, 'Same phone or identity')
                else:
                    user_fact = UserFacts(phonenumber=phonenumber, identitynumber=identity, user=user)

                    user.save()
                    user_fact.save()

                    login(request, user)

                    return redirect('travel-home')
        else:
            messages.warning(request, 'Password should have 8 characters.')
    else:
        return render(request, 'users/register.html')    
    return render(request, 'users/register.html')

def loginUser(request):
    if request.method == 'POST':           
        email = request.POST['email'] 
        password = request.POST['password']  

        username = User.objects.filter(email=email).first().username

        user = authenticate(username=username, password=password)
        if user is not None:                        
            login(request, user)
            return redirect('travel-home')
        else:
            messages.warning(request, "There is no user.")
            return redirect('login')        
    else:
        return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return render(request, 'users/logout.html')
        