from django.contrib import admin
from .models import Genre, Base, Movies, Series

admin.site.register(Genre)
admin.site.register(Base)
admin.site.register(Movies)
admin.site.register(Series)

# Register your models here.
