from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("merhaba")
