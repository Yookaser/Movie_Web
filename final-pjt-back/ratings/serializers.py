from rest_framework import serializers
from .models import MovieRating
from movies.models import Movie


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieRating
        fields = ('pk', 'user', 'movie', 'content', 'rank', 'created_at', 'updated_at',)
        read_only_fields = ('user', 'movie', 'dislike_users')


class RecommendSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'genres', 'title', 'release_date', 'vote_average', 'vote_count', 'poster_path',)

    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = MovieRating
        fields = ('pk', 'user', 'movie', 'content', 'rank', 'created_at', 'updated_at',)
        read_only_fields = ('user', 'movie', 'dislike_users')