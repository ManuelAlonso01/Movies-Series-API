from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movies, Series
from .serializers import MovieSerializer, SeriesSerializer

# Create your views here.

@api_view(['GET'])
def movies_list(request):
    movies = Movies.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response({"Peliculas": serializer.data})

@api_view(['GET'])
def series_list(request):
    series = Series.objects.all()
    serializer = SeriesSerializer(series, many=True)
    return Response({"Series": serializer.data})