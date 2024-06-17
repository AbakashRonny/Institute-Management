from django.shortcuts import render,redirect,HttpResponse
from . forms import RegisterForm,LoginForm
from datetime import datetime
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from . forms import SignUp
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.

def base(request):
    return render(request,'CodeDaisApp/base.html')

def signup_view(request):
    if request.method=="POST":
        f=SignUp(request.POST)
        if f.is_valid():
            f.save()
            d={'register_status':True}
            return render(request,'SignUp_SignIn_App/success.html',d)
        
    else:
        f=SignUp()
        d={'form':f}
        return render(request,'SignUp_SignIn_App/signup.html',d)
    return render(request,'SignUp_SignIn_App/signup.html',{'form':f})

def login_view(request):
    if request.method=='POST':
        f=AuthenticationForm(request=request,data=request.POST)
        if f.is_valid():
            username=f.cleaned_data['username']
            password=f.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user !=None:
                login(request,user)
                return HttpResponseRedirect('/SignUp_SignIn_App/dashboard/')
            
    elif request.user.is_authenticated:
        return HttpResponseRedirect('/SignUp_SignIn_App/dashboard/')
                

    else:
        f=AuthenticationForm()
    return render(request,'SignUp_SignIn_App/login.html',{'form':f})

def home(request):
    return render(request,'CodeDaisApp/home.html')

def course(request):
    return render(request,'CodeDaisApp/course.html')

def blog(request):
    date=datetime.now()
    d={'date':date}
    return render(request,'CodeDaisApp/blog.html',d)

def about(request):
    return render(request,'CodeDaisApp/about.html')