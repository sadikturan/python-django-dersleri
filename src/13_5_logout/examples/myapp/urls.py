from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="products"),
    path('index', views.index),
    path('create', views.create),
    path('edit/<int:id>', views.edit, name="product_edit"),
    path('delete/<int:id>', views.delete, name="product_delete"),
    path('list', views.list, name="product_list"),
    path('upload', views.upload, name="upload_image"),
    path('<slug:slug>', views.details, name="product_details"),
]