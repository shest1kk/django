from django.contrib import admin
from .models import Actors, Categories, Cinemas, Genre, Movie, RatingFilm, ReviewsFilm

admin.site.register(Actors)
admin.site.register(Categories)
admin.site.register(Cinemas)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(RatingFilm)
admin.site.register(ReviewsFilm)