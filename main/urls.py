from django.urls import path
from . import views
from .views import MoviesAPIView, AnimationView, OnlyMoviesView, ComedyGenreView, HorrorGenreView, CartoonGenreView, \
    ActionFilmGenreView, FantasticGenreView, TrillerGenreView, SearchBar, MoviesView, MovieDetailView, AddReview, \
    MoviesDetailAPIView, ReviewsCreateFilmAPIView, MoscinoSaturn, CinemasAPIView, CinemasCreateAPIView

urlpatterns = [
    path('', MoviesView.as_view()),
    path('moscino-saturn', MoscinoSaturn.as_view()),
    path('animations/', AnimationView.as_view()),
    path('films/', OnlyMoviesView.as_view()),
    path('comedy/', ComedyGenreView.as_view()),
    path('horror/', HorrorGenreView.as_view()),
    path('cartoon/', CartoonGenreView.as_view()),
    path('action_film/', ActionFilmGenreView.as_view()),
    path('fantastic/', FantasticGenreView.as_view()),
    path('triller/', TrillerGenreView.as_view()),
    path('search/', SearchBar.as_view(), name='search'),
    path("<slug:slug>/", MovieDetailView.as_view(), name="movie_detail"),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('api/v1/movies', MoviesAPIView.as_view()),
    path('api/v1/cinemas', CinemasCreateAPIView.as_view()),
    path('api/v1/movies/<int:pk>', MoviesDetailAPIView.as_view()),
    path('api/v1/review', ReviewsCreateFilmAPIView.as_view())
]
