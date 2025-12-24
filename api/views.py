from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Movies, Series
from .serializers import MovieSerializer, SeriesSerializer, MovieCreateSerializer, SerieCreateSerializer

# Create your views here.

@api_view(['GET'])
def movies_list(request):
    movies = get_list_or_404(Movies)
    serializer = MovieSerializer(movies, many=True)
    return Response({"Peliculas": serializer.data}, status=200)

@api_view(['GET'])    
def series_list(request):
    series = get_list_or_404(Series)
    serializer = SeriesSerializer(series, many=True)
    return Response({"Series": serializer.data}, status=200)
    
@api_view(['GET'])
def movie_detail(request, id):
    movie = get_object_or_404(Movies, pk=id)
    serializer = MovieSerializer(movie)
    return Response({"Pelicula": serializer.data}, status=200)

@api_view(['GET'])
def serie_detail(request, id):
    serie = get_object_or_404(Series, pk=id)
    serializer = SeriesSerializer(serie)
    return Response({"Serie": serializer.data}, 200)


@api_view(['POST'])
def create_movie(request):
    serializer = MovieCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    movie = serializer.save()
    return Response(MovieSerializer(movie).data, status=201)

@api_view(['POST'])
def create_serie(request):
    serializer = SerieCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serie = serializer.save()
    return Response(SeriesSerializer(serie).data, status=201)