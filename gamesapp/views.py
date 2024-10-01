from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
import time,datetime,pyqrcode
from django.contrib import messages
from django.contrib.auth.models import User,auth
def function1(request):
    if request.user.is_authenticated:
        context = {'user_name': request.user.first_name}
    else:
        context = {}
    return render(request, "index.html", context)

def function2(request):
    return render(request,"matches.html")
def function3(request):
    return render(request,"players.html")
def function4(request):
    return render(request,"blog.html")
def function5(request):
    return render(request,"contact.html")
def function6(request):
    return render(request,"index.html")
def function7(request):
    return render(request,"login.html")

def function8(request):
    return render(request,"profile.html")


def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']  # Get Full Name
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already registered')
                return redirect('register')
            else:
                # Create new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = full_name  # Save Full Name as first name
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('login')
    else:
        return render(request, 'index.html')


# Sign In view
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')  # Redirect to a home or dashboard page
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


# Logout view
def logout(request):
    auth.logout(request)
    return redirect('home')