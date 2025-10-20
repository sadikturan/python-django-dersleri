from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "telefon":"telefon kategorisindeki ürünler",
    "bilgisayar":"bilgisayar kategorisindeki ürünler",
    "elektronik":"elektronik kategorisindeki ürünler"
}

def index(request):
    return HttpResponse("index")

def details(request):
    return HttpResponse("details")

def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())

    if category_id > len(category_list):
        return HttpResponseNotFound("yanlış kategori seçimi")
        
    category_name = category_list[category_id-1]
    
    redirect_path = reverse("products_by_category", args= [category_name])
    
    return redirect(redirect_path)

def getProductsByCategory(request, category):
    try:
        category_text = data[category]        
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")

