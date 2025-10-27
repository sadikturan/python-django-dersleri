from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'title': movie.title,
        'description': movie.description,
        'duration': movie.duration
    }
    return JsonResponse(data)
