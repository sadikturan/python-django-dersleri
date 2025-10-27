from .models import Movie
from . import serializers
from rest_framework import generics

class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.MovieCreateSerializer
        return serializers.MovieSerializer

class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.MovieDetailSerializer
        return serializers.MovieUpdateSerializer
    

