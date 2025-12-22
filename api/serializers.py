from rest_framework import serializers
from .models import Base, Movies, Series, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class BaseSerializer(serializers.ModelSerializer):
    # Hay que indicarle que la relacion con generos es
    # de muchos a muchos o (many to many)
    genres = GenreSerializer(many=True)
    class Meta:
        model = Base
        fields = ["title", "genres"]
    
class MovieSerializer(serializers.ModelSerializer):
    base = BaseSerializer()
    
    class Meta:
        model = Movies
        fields = "__all__"
        
class SeriesSerializer(serializers.ModelSerializer):
    base = BaseSerializer()
    
    class Meta:
        model = Series
        fields = "__all__"
    