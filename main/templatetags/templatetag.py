from django import template

from main.models import Categories, Movie

register = template.Library()


@register.simple_tag()
# Вывод категорий на сайте
def get_categories():
    return Categories.objects.all()


@register.inclusion_tag('movies/tags/last_movies.html')
def get_last_movies():
    movies = Movie.objects.order_by('-id')[:5]
    return {'last_movies': movies}
