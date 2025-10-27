from rest_framework import serializers

def validate_title(value):
        if not value.strip():
            raise serializers.ValidationError("Film başlığı boş olamaz.")
        
        if len(value) < 3:
            raise serializers.ValidationError("Film başlığı için en az 3 karakter olmalıdır.")
        
        return value
    
def validate_duration(value):
    if value is not None and value > 500:
        raise serializers.ValidationError("Süre 500 dakikadan uzun olamaz")
    
    return value

def validate_rating(value):
    if value is not None and (value < 0 or value > 10):
        raise serializers.ValidationError("Rating için 0 ile 10 arasında bir değer giriniz.")
    
    return value

def validate_movie(attrs):
    category = attrs.get("category")
    rating = attrs.get("rating")
    duration = attrs.get("duration")

    if category == 'documentary' and rating is None:
        raise serializers.ValidationError({
            'rating': 'Belgeseller için bir rating değeri zorunludur.'
        })
    
    if category == 'series' and duration is not None and duration < 30:
        raise serializers.ValidationError({
            'duration': 'Dizi bölümleri en az 30 dakika olmalıdır.'
        })
    
    return attrs