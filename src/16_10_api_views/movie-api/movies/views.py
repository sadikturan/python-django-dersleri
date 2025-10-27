from .models import Movie
from . import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class MovieListAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = serializers.MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.MovieCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailAPIView(APIView):
    def get_object(self, pk):
        try:        
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return None

    def get(self, request, pk):
        movie = self.get_object(pk)
        if not movie:
            return Response({'detail': 'Film bulunamadı.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.MovieDetailSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        movie = self.get_object(pk)
        if not movie:
            return Response({'detail': 'Film bulunamadı.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.MovieUpdateSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        movie = self.get_object(pk)
        if not movie:
            return Response({'detail': 'Film bulunamadı.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.MovieUpdateSerializer(movie, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        if not movie:
            return Response({'detail': 'Film bulunamadı.'}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response({'detail': 'Film başarıyla silindi.'}, status=status.HTTP_204_NO_CONTENT)

    

