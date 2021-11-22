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
    context = models.TextField()
