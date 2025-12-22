from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movies
from .serializers import MovieSerializer

# Create your views here.

@api_view(['GET'])
def movies_list(request):
    movies = Movies.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response({"Peliculas": serializer.data})