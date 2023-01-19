from django.views.generic import ListView, DetailView


from .models import Movie


class MoviesView(ListView):
    # Список фильмов
    model = Movie
    queryset = Movie.objects.all()
    template_name = 'movies/movie_list.html'


class MovieDetailView(DetailView):
    # Карточка фильма
    model = Movie
    slug_field = "url"
    template_name = 'movies/movie_detail.html'
