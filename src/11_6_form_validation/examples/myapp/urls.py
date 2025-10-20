from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('create', views.create),
    path('list', views.list),
    path('<slug:slug>', views.details, name="product_details"),
]