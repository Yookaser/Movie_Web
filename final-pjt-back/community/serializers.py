from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import MovieReview, ActorReview, MovieComment, ActorComment


class MovieReviewListSerializer(serializers.ModelSerializer):

    def get_username(self, obj):
        return obj.user.username
      
    username = serializers.SerializerMethodField("get_username", read_only=True)
    
    class Meta:
        model = MovieReview
        fields = ('pk', 'user', 'movie', 'like_users', 'dislike_users', 'title', 'created_at', 'updated_at', 'username',)
        

class MovieReviewSerializer(serializers.ModelSerializer):
    
    class CommentSerailizer(serializers.ModelSerializer):

        def get_username(self, obj):
            return obj.user.username

        commentusername = serializers.SerializerMethodField("get_username")

        class Meta:
            model = MovieComment
            fields = ('pk', 'user', 'like_users', 'dislike_users', 'content', 'created_at', 'updated_at', 'commentusername',)

    def get_username(self, obj):
        return obj.user.username
    
    comments = CommentSerailizer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    reviewusername = serializers.SerializerMethodField("get_username")

    class Meta:
        model = MovieReview
        fields = ('pk', 'like_users', 'dislike_users', 'title', 'content', 'created_at', 'updated_at', 'comments', 'comment_count', 'reviewusername',)
        read_only_fields = ('like_users', 'dislike_users')
        

class ActorReviewListSerializer(serializers.ModelSerializer):
    
    def get_username(self, obj):
        return obj.user.username

    username = serializers.SerializerMethodField("get_username")
    
    class Meta:
        model = ActorReview
        fields = ('pk', 'user', 'actor', 'like_users', 'dislike_users', 'title', 'created_at', 'updated_at', 'username')
        

class ActorReviewSerializer(serializers.ModelSerializer):
    
    def get_username(self, obj):
        return obj.user.username

    class CommentSerailizer(serializers.ModelSerializer):

        def get_username(self, obj):
            return obj.user.username

        commentusername = serializers.SerializerMethodField("get_username")

        class Meta:
            model = ActorComment
            fields = ('pk', 'user', 'like_users', 'dislike_users', 'content', 'created_at', 'updated_at', 'commentusername')
    
    comments = CommentSerailizer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)
    reviewusername = serializers.SerializerMethodField("get_username")

    class Meta:
        model = ActorReview
        fields = ('pk', 'like_users', 'dislike_users', 'title', 'content', 'created_at', 'updated_at', 'comments', 'comment_count', 'reviewusername')
        read_only_fields = ('like_users', 'dislike_users')


class MovieCommentSerializer(serializers.ModelSerializer):
    
    def get_username(self, obj):
        return obj.user.username

    commentusername = serializers.SerializerMethodField("get_username")

    class Meta:
        model = MovieComment
        fields = ('pk', 'like_users', 'dislike_users', 'content', 'created_at', 'updated_at', 'commentusername')
        read_only_fields = ('like_users', 'dislike_users')


class ActorCommentSerializer(serializers.ModelSerializer):
    
    def get_username(self, obj):
        return obj.user.username

    commentusername = serializers.SerializerMethodField("get_username")

    class Meta:
        model = ActorComment
        fields = ('pk', 'like_users', 'dislike_users', 'content', 'created_at', 'updated_at', 'commentusername')
        read_only_fields = ('like_users', 'dislike_users')
