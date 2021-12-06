from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_request, name="login"),
    path('register', views.register_request, name="register"),
    path('change_password', views.change_password, name="change_password"),
    path('logout', views.logout_request, name="logout"),
]
