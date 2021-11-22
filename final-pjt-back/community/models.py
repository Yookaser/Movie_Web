from django.db import models
from django.conf import settings
from movies.models import Movie, Actor


class MovieReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie_reviews')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_movie_reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ActorReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, related_name='reviews' ,on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actor_reviews')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_actor_reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MovieComment(models.Model):
    review = models.ForeignKey(MovieReview, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie_comments')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_movie_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ActorComment(models.Model):
    review = models.ForeignKey(ActorReview, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actor_comments')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_actor_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
