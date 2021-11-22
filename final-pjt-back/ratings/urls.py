from django.urls import path
from . import views


urlpatterns = [
    path('movie/<int:movie_pk>/', views.movie_rating_read),
    path('movie/<int:movie_pk>/create/', views.movie_rating_create),
    path('movie/<int:rating_pk>/update/', views.movie_rating_update),
    path('movie/<int:movie_pk>/<int:user_pk>/', views.movie_rating_check),
    path('recommend/<int:user_pk>/', views.movie_recommend),
]
