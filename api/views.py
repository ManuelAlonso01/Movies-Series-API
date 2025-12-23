from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Movies, Series
from .serializers import MovieSerializer, SeriesSerializer

# Create your views here.

@api_view(['GET'])
def movies_list(request):
    movies = get_list_or_404(Movies)
    serializer = MovieSerializer(movies, many=True)
    return Response({"Peliculas": serializer.data}, 200)

@api_view(['GET'])    
def series_list(request):
    series = get_list_or_404(Series)
    serializer = SeriesSerializer(series, many=True)
    return Response({"Series": serializer.data}, 200)
    
@api_view(['GET'])
def movie_detail(request, id):
    movie = get_object_or_404(Movies, pk=id)
    serializer = MovieSerializer(movie)
    return Response({"Pelicula": serializer.data}, 200)

@api_view(['GET'])
def serie_detail(request, id):
    serie = get_object_or_404(Series, pk=id)
    serializer = SeriesSerializer(serie)
    return Response({"Serie": serializer.data}, 200)
    