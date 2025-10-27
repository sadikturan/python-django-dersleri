from django.shortcuts import render
from .models import Movie
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = serializers.MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializers.MovieCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH'])
def movie_detail(request, pk):
    try:        
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'detail': 'Film bulunamadı.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = serializers.MovieDetailSerializer(movie)
        return Response(serializer.data)
    
    partial = request.method == 'PATCH'
    serializer = serializers.MovieUpdateSerializer(movie, data=request.data, partial=partial)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

