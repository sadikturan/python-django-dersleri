from django.shortcuts import render

from account.forms import LoginForm

# Create your views here.
def login_request(request):
    form = LoginForm()
    return render(request, 'account/login.html',{'form':form})

def register_request(request):
    return render(request, 'account/register.html')

def change_password(request):
    return render(request, 'account/change_password.html')

def logout_request(request):
    pass