from django.urls import path
from .views import movies_list, series_list, movie_detail, serie_detail, create_movie, create_serie

urlpatterns = [
    path("movies/", movies_list),
    path("series/", series_list),
    path("movies/<int:id>/", movie_detail),
    path("series/<int:id>/", serie_detail),
    path("movies/create/", create_movie),
    path("serie/create/", create_serie),
    
]