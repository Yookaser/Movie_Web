from rest_framework import serializers
from .models import Genre, Movie, Actor


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('pk', 'key', 'name',)


class ActorSerializer(serializers.ModelSerializer):
    
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'release_date')
    
    movies = MovieSerializer(many=True, read_only=True)
    movie_count = serializers.IntegerField(source='movies.count', read_only=True)

    class Meta:
        model = Actor
        fields = ('pk', 'name', 'gender', 'birth_date', 'birth_place', 'profile_path', 'movies', 'movie_count')


class MovieSerializer(serializers.ModelSerializer):
    
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('pk', 'name',)
        
    
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('pk', 'name',)

    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    genres_list = serializers.ListField(write_only=True)
    actors_list = serializers.ListField(write_only=True)
    
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'release_date', 'vote_average', 'vote_count', 'poster_path', 'genres', 'actors', 'genres_list', 'actors_list')
    

    def create(self, validated_data):
        genres_list = validated_data.pop('genres_list')
        actors_list = validated_data.pop('actors_list')
        movie = Movie.objects.create(**validated_data)
        for artist_pk in genres_list:
            movie.genres.add(artist_pk)
        for artist_pk in actors_list:
            movie.actors.add(artist_pk)
        return movie
