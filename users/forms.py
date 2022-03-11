from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterationForm(UserCreationForm):
    phonenumber = forms.CharField(max_length=20)
    email = forms.EmailField()
    identitynumber = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ['username', 'phonenumber', 'email', 'identitynumber', 'password1', 'password2']