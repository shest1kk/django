from django.urls import path
from . import views
from .views import MoviesAPIView

urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('api/v1/movielist', MoviesAPIView.as_view()),
]