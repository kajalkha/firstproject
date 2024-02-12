from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def base(request):
    return render(request,'userapp/index.html')

def login_data(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            request.session['test'] = 'testing user session'
        return redirect('/home')
    else:
        logout(request)
        redirect('/login')
    return render(request,'userapp/login.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(
            username=username,
            email=email,
            password=password
            )
        return redirect('/register')
    return render(request,'userapp/register.html')


def logout_data(request):
    logout(request)
    return redirect('/login')