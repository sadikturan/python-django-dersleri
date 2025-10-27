from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title','category','rating','release_date']

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title','description','release_date','duration','rating','poster','category']

