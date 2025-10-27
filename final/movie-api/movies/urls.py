from django.urls import path
from . import views

# movies    => GET
# movies    => POST
# movies/1    => GET 
# movies/1    => PUT, PATCH 
# movies/1    => DELETE

urlpatterns = [
    path('', views.MovieListAPIView.as_view(), name='movies_list'),
    path('<int:pk>', views.MovieDetailAPIView.as_view(), name='movie_detail')
]
