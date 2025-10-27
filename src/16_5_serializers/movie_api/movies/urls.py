from django.urls import path
from .views import movie_list, movie_detail

urlpatterns = [
    path('', movie_list, name='movies_list'),
    path('<int:pk>', movie_detail, name='movie_detail')
]
