from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Product

def index(request):
    products = Product.objects.all().order_by("-price")

    context = {
        "products": products,
    }

    return render(request, 'index.html', context)

def list(request):
    if request.GET['q'] and request.GET['q'] is not None:
        q = request.GET['q']
        products = Product.objects.filter(name__contains=q).order_by("-price")
    else:
        return HttpResponseRedirect("/products")

    context = {
        "products": products,
    }

    return render(request, 'list.html', context)

def details(request, slug):

    product = get_object_or_404(Product, slug=slug)

    context = {
        "product": product
    }
    return render(request, "details.html", context)




