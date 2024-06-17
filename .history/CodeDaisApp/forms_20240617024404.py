from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.Form):
    Name=forms.CharField()
    Email=forms.EmailField()
    Mobile=forms.IntegerField()
    College=forms.CharField()
    Password=forms.CharField()

class LoginForm(forms.Form):
    Email=forms.EmailField()
    Password=forms.CharField()


class SignUp(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password1','password2','email','first_name','last_name')

