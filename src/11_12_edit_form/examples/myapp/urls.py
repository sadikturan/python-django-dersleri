from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('create', views.create),
    path('edit/<int:id>', views.edit, name="product_edit"),
    path('list', views.list, name="product_list"),
    path('<slug:slug>', views.details, name="product_details"),
]