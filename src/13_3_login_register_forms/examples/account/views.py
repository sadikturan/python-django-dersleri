from django.shortcuts import redirect, render

# Create your views here.

def login_request(request):
    if request.method == "POST":
        # login
        pass
    else:
        return render(request, "account/login.html")

def register_request(request):
    if request.method == "POST":
        # register
        pass
    else:
        return render(request, "account/register.html")

def logout_request(request):
    return redirect("products")