from rest_framework import serializers
from .models import Review, Comment


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('pk', 'user', 'like_users', 'dislike_users', 'title', 'created_at', 'updated_at',)


class ReviewSerializer(serializers.ModelSerializer):
    
    class CommentSerailizer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('pk', 'user', 'like_users', 'dislike_users', 'content', 'created_at', 'updated_at',)
    
    comments = CommentSerailizer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'like_users', 'dislike_users', 'title', 'content', 'created_at', 'updated_at', 'category', 'comments', 'comment_count',)
        

class ReviewLikeUserserializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('pk', 'like_users')
    

class ReviewDislikeUserserializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('pk', 'dislike_users')


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('pk', 'review', 'user', 'like_users', 'dislike_users', 'content', 'created_at', 'updated_at', 'category')
        read_only_fields = ('review',)
