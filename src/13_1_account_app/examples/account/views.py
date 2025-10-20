from django.shortcuts import redirect, render

# Create your views here.

def login(request):
    return render(request, "account/login.html")

def register(request):
    return render(request, "account/register.html")

def logout(request):
    return redirect("products")