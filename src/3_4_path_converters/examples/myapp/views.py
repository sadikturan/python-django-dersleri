from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("index")

def details(request):
    return HttpResponse("details")

def list(request):
    return HttpResponse("list")

def getProductsByCategoryId(request, category):
    return HttpResponse(category)

def getProductsByCategory(request, category):
    category_text = None
    if category == 'bilgisayar':
        category_text = "bilgisayar kategorisindeki ürünler"
    elif category == 'telefon':
        category_text = 'telefon kategorisindeki ürünler'
    else:
        category_text = 'yanlış kategori seçimi'
        
    return HttpResponse(category_text)

