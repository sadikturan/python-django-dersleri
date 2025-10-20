from datetime import date
from django.shortcuts import render

from movies.models import Movie

data = {   
    "sliders": [
        {
            "slider_image": "slider1.jpg",
            "url": "film-adi-1"
        },
         {
            "slider_image": "slider2.jpg",
            "url": "film-adi-2"
        },
         {
            "slider_image": "slider3.jpg",
            "url": "film-adi-3"
        }
    ]
}

# Create your views here.

def index(request):
    movies = Movie.objects.filter(is_active=True,is_home=True)
    sliders = data["sliders"]
    return render(request, 'index.html', {
        "movies": movies,
        "sliders": sliders
    })

def movies(request):
    movies = Movie.objects.filter(is_active=True)
    return render(request, 'movies.html', {
        "movies": movies
    })

def movie_details(request, slug):
    movies = data["movies"]
    # selectedMovie = None
    # for movie in movies:
    #     if movie["slug"] == slug:
    #         selectedMovie = movie

    selectedMovie = next(movie for movie in movies if movie["slug"] == slug)

    return render(request, 'movie-details.html', {
        "movie": selectedMovie
})