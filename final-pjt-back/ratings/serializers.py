from rest_framework import serializers
from .models import MovieRating
from movies.models import Movie


class RatingSerializer(serializers.ModelSerializer):

    def get_username(self, obj):
        return obj.user.username
      
    username = serializers.SerializerMethodField("get_username", read_only=True)
    
    class Meta:
        model = MovieRating
        fields = ('pk', 'user', 'movie', 'content', 'rank', 'created_at', 'updated_at', 'username')
        read_only_fields = ('user', 'movie')
