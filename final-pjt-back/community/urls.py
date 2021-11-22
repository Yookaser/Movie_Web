from django.urls import path
from . import views


urlpatterns = [
    path('reviews/movie/list/', views.movie_review_read_all),
    path('reviews/movie/list/<int:movie_pk>/', views.movie_review_read),
    path('reviews/movie/create/<int:movie_pk>/', views.movie_review_create),
    path('reviews/movie/<int:review_pk>/', views.movie_review_read_update_delete),

    path('reviews/actor/list/', views.actor_review_read_all),
    path('reviews/actor/list/<int:actor_pk>/', views.actor_review_read),
    path('reviews/actor/create/<int:actor_pk>/', views.actor_review_create),
    path('reviews/actor/<int:review_pk>/', views.actor_review_read_update_delete),

    path('reviews/movie/<int:review_pk>/comment/', views.movie_create_comment),
    path('reviews/movie/comment/<int:comment_pk>/', views.movie_comment_update_delete),
    path('reviews/actor/<int:review_pk>/comment/', views.actor_create_comment),
    path('reviews/actor/comment/<int:comment_pk>/', views.actor_comment_update_delete),

    path('reviews/<category>/<int:review_pk>/<int:flag>/', views.like_dislike),

    path('user/movie/reviews/<int:user_pk>/', views.user_movie_review),
    path('user/actor/reviews/<int:user_pk>/', views.user_actor_review),
]
