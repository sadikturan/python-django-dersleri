from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from account.forms import LoginUserForm, NewUserForm

def login_request(request):

    if request.user.is_authenticated:
        return redirect("products")
   
    if request.method == "POST":
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect("products")
            else:
                return render(request, 'account/login.html', {'form':form})
        else:
            return render(request, 'account/login.html', {'form':form})
    else:
        form = LoginUserForm()
        return render(request, 'account/login.html', {'form':form})
        
        

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect("products")
        else:
            return render(request, "account/register.html", {"form":form})
    form = NewUserForm()
    return render(request, "account/register.html", {"form":form})

def logout_request(request):
    logout(request)
    messages.success(request, "uygulamadan çıkıldı.")
    return redirect("products")