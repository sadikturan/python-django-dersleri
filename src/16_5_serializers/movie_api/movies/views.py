from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer, MovieDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)
