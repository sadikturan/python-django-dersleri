from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
import datetime

data = {
    "telefon": ["samsung s20","samsung s21","iphone 12"],
    "bilgisayar": ["laptop 1","laptop 2"],
    "elektronik": []
}

def index(request):
    categories = list(data.keys())

    return render(request, 'index.html', {
        "categories": categories
    })

def getProductsByCategoryId(request, category_id):
    category_list = list(data.keys())

    if category_id > len(category_list):
        return HttpResponseNotFound("yanlış kategori seçimi")
        
    category_name = category_list[category_id-1]
    
    redirect_path = reverse("products_by_category", args= [category_name])
    
    return redirect(redirect_path)

def getProductsByCategory(request, category):
    try:
        products = data[category]        
        return render(request, 'products.html', {
            "category": category,
            "products": products,
            "now": datetime.datetime.now()
        })
    except:
        return HttpResponseNotFound(f"<h1>yanlış kategori seçimi</h1>")

