from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Product
from .forms import ProductCreateForm

def index(request):
    products = Product.objects.filter(isActive=True).order_by("-price")

    context = {
        "products": products,
    }

    return render(request, 'index.html', context)

def list(request):
    if 'q' in request.GET and request.GET.get('q'):
        q = request.GET['q']
        products = Product.objects.filter(name__contains=q).order_by("-price")
    else:
        products = Product.objects.all().order_by("-price")

    context = {
        "products": products,
    }

    return render(request, 'list.html', context)

def create(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        price = request.POST['price']
        description = request.POST['description']
        slug = request.POST['slug']
        error = False

        if(product_name == "" or len(product_name) <= 10):
            error = True

        if(error):
            return render(request,"create.html", {
                "error": True
            })
        else:
            p = Product(name= product_name, description = description, price= price, imageUrl="1.jpg", slug=slug)
            p.save()
            return HttpResponseRedirect("list") 

    form = ProductCreateForm()
        
    return render(request, "create.html", {
        "form": form
    })

def details(request, slug):

    product = get_object_or_404(Product, slug=slug)

    context = {
        "product": product
    }
    return render(request, "details.html", context)




