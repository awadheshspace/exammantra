from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home_page(request):
    return render(request, "login/home.html")


def signup_page(request):
    if request.method=='POST':
        fname=request.POST.get('fullname')
        email=request.POST.get('email')
        uname=request.POST.get('username')
        password1=request.POST.get('password')
        cpasswaord=request.POST.get('confirm-password')

        if password1 != cpasswaord:
            return HttpResponse(f"Sorry , {fname} You have Entered mismatch Password \n Try Again")

        else:
            my_user= User.objects.create_user(fname,uname,password1)
            my_user.save()
            return redirect('login')


        # return HttpResponse(f"Hii,{fname} \n you have been created your account Successfully!!!!")
    
    return render(request, "login/signup.html")

def login_page(request):
    if request.method== 'POST' :
        uname=request.POST.get('username')
        password1=request.POST.get('password')
        user = authenticate(request, username=uname, password=password1)
        if user is None:
            return HttpResponse(f"You have Entered Wrong Credential !!")
           
        else:
            login(request,user)
            return redirect('home')

    return render(request, "login/login.html")


def logout_page(request):
    logout(request)
    return redirect('login')

def dashboard_page(request):
    return render(request,'login/dashboard.html')

def index_page(request):
    return render(request,'login/index.html')    