from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Userinfo, UserMovie
from movies.models import Movie


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class UserAdditionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Userinfo
        fields = ('pk', 'user', 'nickname', 'birth_date', 'context')
        read_only_fields = ('user',)


class UserMovieserializer(serializers.ModelSerializer):

    def get_title(self, obj):
        return obj.movie.title

    def get_poster(self, obj):
        return obj.movie.poster_path
    
    title = serializers.SerializerMethodField("get_title", read_only=True)
    poster_path = serializers.SerializerMethodField("get_poster", read_only=True)

    class Meta:
        model = UserMovie
        fields = ('pk', 'user', 'movie', 'created_at', 'title', 'poster_path')
