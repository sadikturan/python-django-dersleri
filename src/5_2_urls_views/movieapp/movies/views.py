from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("index")

def movies(request):
    return HttpResponse("movies")

def movie_details(request, slug):
    return HttpResponse("movie_details: " + slug)