from django.db import models
from movies.models import Movie
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Userinfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=30)
    birth_date = models.DateField()
    context = models.TextField(max_length=150)
    # image = models.ImageField()


class UserMovie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
