from django.forms import model_to_dict
from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

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

class MoviesAPIView(APIView):

    def get(self, request):
        queryset = Movie.objects.all()
        return Response({'films': MovieSerializer(queryset, many=True).data})

    def post(self, request):
        new_entry = Movie.objects.create(
            year = request.data['year'],
            title = request.data['title'],
            category = request.data['name'],
            genre = request.data['genre'],
            description = request.data['description'],
            contry = request.data['country'],
            actors = request.data['actors'],
        )

        return Response({'films': model_to_dict(new_entry)})