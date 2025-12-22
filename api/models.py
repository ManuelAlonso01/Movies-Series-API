from django.db import models

# Tabla generos
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Tabla base    
class Base(models.Model):
    MOVIE = "movie"
    SERIES = "series"
    
    TYPE_CHOICES = [    
        (MOVIE, "Pelicula"),
        (SERIES, "Serie"),
    ]
    
    title = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10, choices=TYPE_CHOICES)
    genres = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title
    
    
# Tabla Movies
class Movies(models.Model):
    base = models.OneToOneField(
        Base,
        on_delete=models.CASCADE,
        related_name="movie"     
    )
    # CASCADE indica que si se borra la base de la pelicula
    # la pelicula tambien se borre
    # related_name es para poder acceder a la pelicula como base.movie
    year = models.IntegerField()
    director = models.CharField(max_length=150)
    duration_minutes = models.IntegerField()
    
    def __str__(self):
        return f"{self.base.title} (Movie)"

class Series(models.Model):
    base = models.OneToOneField(
        Base,
        on_delete=models.CASCADE,
        related_name="series"
    )
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    # [null=True (puede ser null en db)],
    # [blank=True (puede estar vacio en formularios)]
    # Series en emision no tienen end_year
    season_count = models.IntegerField()
    episodes_count = models.IntegerField()
    
    def __str__(self):
        return f"{self.base.title} (Series)"