from django.shortcuts import render,redirect
from myapp.models import customuser
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def registerpage(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        username=request.POST.get('username')
        role=request.POST.get('role')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        user_exists=customuser.objects.filter(username=username).exists()
        if user_exists:
            return redirect('registerpage')
        if password==confirm_password:
            user=customuser.objects.create_user(
                full_name=fullname,
                username=username,
                password=password,
                roles=role
            )
           
    return render(request,'auth/signin.html')
def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('homepage')
    return render(request,'auth/login.html')
def logoutpage(request):
    logout(request)
    return redirect('loginpage')

    



