from django.shortcuts import render,redirect,HttpResponse
from . forms import RegisterForm,LoginForm
from datetime import datetime
# Create your views here.

def base(request):
    return render(request,'CodeDaisApp/base.html')

def register(request):
    if request.method=='POST':
        # Capture the Data
        Name=request.POST['Name']
        Email=request.POST['Email']
        Mobile=request.POST['Mobile']
        College=request.POST['College']
        Password=request.POST['Password']
        # Store inside session
        request.session['Name']=Name
        request.session['Email']=Email
        request.session['Mobile']=Mobile
        request.session['College']=College
        request.session['Password']=Password
    f=RegisterForm()
    d={'form':f}
    return render(request,'CodeDaisApp/registration.html',d)

def login(request):
    if request.method=='POST':
        Email=request.POST['Email']
        Password=request.POST['Password']
        if request.session['Email']==Email and request.session['Password']==Password:
            return redirect('home')
        else:
            return HttpResponse('<h2>Invalid Email or Password</h2>')
    f=LoginForm()
    d={'form':f}
    return render(request,'CodeDaisApp/login.html',d)

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