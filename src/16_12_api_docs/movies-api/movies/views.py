from .models import Movie
from . import serializers
from rest_framework import generics
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    get=extend_schema(summary="Film listesini getir.", tags=['Movies']),
    post=extend_schema(summary="Yeni film ekle.", tags=['Movies'])
)
class MovieListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.MovieCreateSerializer
        return serializers.MovieSerializer

@extend_schema_view(
    get=extend_schema(summary="Belirli bir filmi getirir.", tags=['Movies']),
    put=extend_schema(summary="Belirli bir filmi günceller.", tags=['Movies']),
    patch=extend_schema(summary="Belirli bir filmi parçalı olarak günceller.", tags=['Movies']),
    delete=extend_schema(summary="Bir filmi siler.", tags=['Movies'])
)
class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.MovieDetailSerializer
        return serializers.MovieUpdateSerializer
    

