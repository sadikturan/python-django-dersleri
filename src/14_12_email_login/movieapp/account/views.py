from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from account.forms import LoginForm
from django.contrib.auth.models import User

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home_page")
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home_page")
            else:
                return render(request, 'account/login.html',{'form':form})
        else:
            return render(request, 'account/login.html',{'form':form})


    form = LoginForm()
    return render(request, 'account/login.html',{'form':form})

def register_request(request):
    return render(request, 'account/register.html')

def change_password(request):
    return render(request, 'account/change_password.html')

def logout_request(request):
    pass