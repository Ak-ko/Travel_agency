from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import UserFacts

class RegisterationForm(UserCreationForm):
    phonenumber = forms.CharField()
    email = forms.EmailField()
    identitynumber = forms.CharField()

    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {"type" : "password"}
    ))

    phonenumber = forms.CharField(widget=forms.TextInput(
        attrs= {"type" : "number"}
    ))

    def __init__(self, *args, **kwargs):
        super(RegisterationForm, self).__init__(*args, **kwargs)
        
        self.fields["username"].widget.attrs.update({
            'placeholder' : 'Username',
            'class' : 'username inputs',
            'autocomplete' : 'off'
            
        })        

        self.fields["email"].widget.attrs.update({
            'placeholder' : 'Email',
            'class' : 'email inputs',
            'autocomplete' : 'off'
            
        })

        self.fields["password"].widget.attrs.update({            
            'placeholder' : 'password',
            'class' : 'password inputs',
            'autocomplete' : 'off'            
            
        })
    
    class Meta:
        model = User
        fields = ['username','email', 'password']

class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(max_length=20)

        # can add like this.

    # email = forms.EmailField(widget=forms.TextInput(
    #     attrs={'class': 'inputs', 'placeholder': 'Email', 'class': 'email', 'autocomplete' : 'off'} 
    #     ))

    # password = forms.CharField(widget=forms.PasswordInput(
    #     attrs={
    #         'class': 'inputs',
    #         'placeholder': 'Password',
    #         'class' : 'password'
    #     }
    # ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({
                'placeholder' : 'Email',
                'class' : 'email inputs',
                'autocomplete' : 'off'
                
        })

        self.fields["password"].widget.attrs.update({
            'placeholder' : 'password',
            'class' : 'password inputs',
            'autocomplete' : 'off'            
            
        })

class UserFactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserFactForm,self).__init__(*args, **kwargs)

        self.fields["phonenumber"].widget.attrs.update({   
            'placeholder' : 'Phone number',
            'class' : 'phonenumber inputs',
            'autocomplete' : 'off'            
        })

        self.fields["identitynumber"].widget.attrs.update({
            'placeholder' : 'Identity number',
            'class' : 'identitynumber inputs',
            'autocomplete' : 'off'
        })

        
        
    class Meta:
        model = UserFacts
        fields = ['phonenumber', 'identitynumber', 'visa', 'cvv']


    
