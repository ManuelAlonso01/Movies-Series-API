from django.urls import path
from .views import movies_list, series_list

urlpatterns = [
    path("movies/", movies_list),
    path("series/", series_list),
]