from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
import datetime
from .models import Product
from django.db.models import Avg, Min, Max

data = {
    "telefon": ["samsung s20","samsung s21","iphone 12"],
    "bilgisayar": ["laptop 1","laptop 2"],
    "elektronik": []
}

def index(request):
    products = Product.objects.all().order_by("-price")
    product_count = Product.objects.filter(isActive=True).count()
    price = Product.objects.filter(isActive=True).aggregate(Avg("price"), Min("price"), Max("price"))

    context = {
        "products": products,
        "product_count": product_count,
        "price" : price
    }

    return render(request, 'index.html', context)

def details(request, slug):

    product = get_object_or_404(Product, slug=slug)

    context = {
        "product": product
    }
    return render(request, "details.html", context)

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

