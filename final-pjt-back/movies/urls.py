from django.urls import path
from . import views


urlpatterns = [
    path('genres/', views.genre_read_or_create),
    path('actors/', views.actor_read_or_create),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('movies/', views.movie_read_create),
    path('movies/<int:movie_pk>/', views.moive_detail),
]
