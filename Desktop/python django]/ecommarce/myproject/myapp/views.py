from django.shortcuts import render,redirect
from myapp.models import customuser
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import customuser
from django.contrib import messages
def registerpage(request):
    
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get("confirm_password")
        user_type= request.POST.get("user_type")  
        user_exists = customuser.objects.filter(username=username).exists()
        if user_exists:
            messages.warning(request,"user already exists")
            return redirect("registerpage")
        if password==confirm_password:
            user=customuser.objects.create_user(
              fullname=fullname,  
              email=email,
              username=username,
              password=password,
              user_type=user_type
            
            )
            messages.success(request,"user crteated successfully")
            return redirect("loginpage")
        else:
            messages.warning(request,'password not matched.')
        return redirect ("registerpage")
           
    return render(request,"auth/signin.html")

def loginpage(request): 
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("master/home.html")
            
                                  
    return render(request,'auth/login.html') 

def logoutpage(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("loginpage")

def homepage(request):
    return render(request,"master/home.html")