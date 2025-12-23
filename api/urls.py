from django.urls import path
from .views import movies_list, series_list, movie_detail, serie_detail

urlpatterns = [
    path("movies/", movies_list),
    path("series/", series_list),
    path("movies/<int:id>/", movie_detail),
    path("series/<int:id>/", serie_detail),
]