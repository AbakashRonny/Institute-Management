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