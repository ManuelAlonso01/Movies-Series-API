from rest_framework import serializers
from .models import Movies, Series
    
class MovieSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="base.title")
    genres = serializers.SlugRelatedField(
        source="base.genres",
        many=True,
        read_only=True,
        slug_field="name",
    )
    class Meta:
        model = Movies
        fields = [
            "id",
            "title",
            "genres",
            "year",
            "director",
            "duration_minutes",
        ]
    
            
class SeriesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="base.title")
    genres = serializers.SlugRelatedField(
        source="base.genres",
        many=True,
        read_only=True,
        slug_field="name",
    )
    class Meta:
        model = Series
        fields = [
            "id",
            "title",
            "genres",
            "start_year",
            "end_year",
            "season_count",
            "episodes_count",
        ]
    