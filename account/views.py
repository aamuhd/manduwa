
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from core.models import UserProfile


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'username or password is not correct')
            return redirect('/account/login/')

    else:
        return render(request, 'account/login.html')


def register(request):


    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username exists')
                return redirect('/account/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
                return redirect(request, '/account/register/')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username,
                    email=email, password=password1
                
                )

                user.save()

                return redirect('/')
    
    else:
        return render(request, 'account/register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

