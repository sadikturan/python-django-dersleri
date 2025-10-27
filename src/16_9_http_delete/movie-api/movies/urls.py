from django.urls import path
from .views import movie_list, movie_detail

# movies    => GET
# movies    => POST
# movies/1    => GET 
# movies/1    => PUT, PATCH 
# movies/1    => DELETE

urlpatterns = [
    path('', movie_list, name='movies_list'),
    path('<int:pk>', movie_detail, name='movie_detail')
]
