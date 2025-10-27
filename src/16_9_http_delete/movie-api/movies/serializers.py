from rest_framework import serializers
from .models import Movie
from . import validations

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

    def validate_title(self, value):
        return validations.validate_title(value)
    
    def validate_duration(self, value):
        return validations.validate_duration(value)
    
    def validate_rating(self, value):
        return validations.validate_rating(value)
    
    def validate(self, values):
        return validations.validate_movie(values)
    
class MovieUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title','description','release_date','duration','rating','poster','category']

    def validate_title(self, value):
        return validations.validate_title(value)
    
    def validate_duration(self, value):
        return validations.validate_duration(value)
    
    def validate_rating(self, value):
        return validations.validate_rating(value)
    
    def validate(self, values):
        return validations.validate_movie(values)

    


