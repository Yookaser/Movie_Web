from django.urls import path
from . import views


urlpatterns = [
    path('reviews/movie/list/<int:movie_pk>/', views.movie_review_read_all),
    path('reviews/movie/create/<int:movie_pk>/', views.movie_review_create),
    path('reviews/movie/<int:review_pk>/', views.movie_review_read_update_delete),

    path('reviews/actor/list/<int:actor_pk>/', views.actor_review_read_all),
    path('reviews/actor/create/<int:actor_pk>/', views.actor_review_create),
    path('reviews/actor/<int:review_pk>/', views.actor_review_read_update_delete),

    path('reviews/movie/<int:review_pk>/comment/', views.movie_create_comment),
    path('reviews/actor/<int:review_pk>/comment/', views.actor_create_comment),

    path('reviews/<category>/<int:review_pk>/<int:flag>/', views.like_dislike),

    # path('reviews/<int:review_pk>', views.review_detail_update_delete),
    # path('reviews/<int:review_pk>/comment/<int:comment_pk>/', views.comment_update_delete),
]
