from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
    # nickname = models.TextField(max_length=30)
    # birth_date = models.DateField()
