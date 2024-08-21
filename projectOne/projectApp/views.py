from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
# Create your views here.

# def home(request):
    # return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')
    return render(request, 'login.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmPassword')

        if pass1!=pass2:
            return HttpResponse('<h1>you password and comfrom password is not same</h1>')
        else:
             my_user=User.objects.create_user(username,email,pass1)
             my_user.save()
        # return HttpResponse("User has been create sucessfull")
             return redirect('login')

        # print(username,email,pass1,pass2)

    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')