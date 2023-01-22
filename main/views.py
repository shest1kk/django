
from django.shortcuts import redirect, render
from django.forms import model_to_dict
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import ReviewForm
from .models import Movie, Genre, Categories
from .serializers import MovieSerializer


class GenreYears:
    """Жанры и года выхода фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.values("year")


class MoviesView(GenreYears, ListView):
    # Список фильмов
    model = Movie
    queryset = Movie.objects.all()
    paginate_by = 6
    ordering = ['-id']
    template_name = 'movies/movie_list.html'

class AnimationView(ListView):
    model = Movie
    queryset = Movie.objects.filter(category_id = 2)
    paginate_by = 6
    ordering = ['-id']
    template_name = 'movies/animation_list.html'


class OnlyMoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(category_id = 1)
    paginate_by = 6
    ordering = ['-id']
    template_name = 'movies/onlymovies_list.html'
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Categories.objects.all()
    #     return context

class ComedyGenreView(ListView):
    model = Movie
    queryset = Movie.objects.filter(genre__url='comedy')
    paginate_by = 6
    template_name = 'movies/comedy_list.html'

class HorrorGenreView(ListView):
    model = Movie
    queryset = Movie.objects.filter(genre__url='horror')
    paginate_by = 6
    template_name = 'movies/horror_list.html'

class CartoonGenreView(ListView):
    model = Movie
    queryset = Movie.objects.filter(genre__url='cartoon')
    paginate_by = 6
    template_name = 'movies/cartoon_list.html'

class ActionFilmGenreView(ListView):
    model = Movie
    queryset = Movie.objects.filter(genre__url='action_film')
    paginate_by = 6
    template_name = 'movies/action_film_list.html'

class FantasticGenreView(ListView):
    model = Movie
    queryset = Movie.objects.filter(genre__url='fantastic')
    paginate_by = 6
    template_name = 'movies/fantastic_list.html'

class TrillerGenreView(ListView):
    model = Movie
    queryset = Movie.objects.filter(genre__url='triller')
    paginate_by = 6
    template_name = 'movies/triller_list.html'

class MovieDetailView(GenreYears, DetailView):
    # Карточка фильма
    model = Movie
    slug_field = "url"
    template_name = 'movies/movie_detail.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Categories.objects.all()
    #     return context


class AddReview(View):
    # Добавление отзыва
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())

class MoviesAPIView(APIView):

    def get(self, request):
        queryset = Movie.objects.all()
        return Response({'films': MovieSerializer(queryset, many=True).data})

    def post(self, request):
        new_entry = Movie.objects.create(
            year=request.data['year'],
            title=request.data['title'],
            category=request.data['name'],
            genre=request.data['genre'],
            description=request.data['description'],
            contry=request.data['country'],
            actors=request.data['actors'],
        )
        return Response({'films': model_to_dict(new_entry)})
