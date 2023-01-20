from rest_framework import serializers
from .models import Movie, Genre, Actors


class MovieSerializer(serializers.Serializer):
    year = serializers.IntegerField(default=2023)
    title = serializers.CharField()
    category_id = serializers.IntegerField()
    # genre = serializers.ListField(child)
    description = serializers.CharField()
    country = serializers.CharField()
    # actors = serializers.ListField()
    image = serializers.ImageField()
    url = serializers.URLField()



