from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')   # login_url='login' keeps the login page if we http://127.0.0.1:8000/home/ if we dont put this it will throw 404
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("password and confirm password didn't match")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

        print(uname, email, pass1, pass2)

    return render(request, 'registration.html')

def loginpage(request):
    
    if request.method == 'POST':
        usname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=usname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("username or password are incorrect")

    return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return redirect('login')