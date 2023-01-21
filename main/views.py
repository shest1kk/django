from django.forms import model_to_dict
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView, DetailView

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import ReviewForm
from .models import Movie, Categories
from .serializers import MovieSerializer


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
