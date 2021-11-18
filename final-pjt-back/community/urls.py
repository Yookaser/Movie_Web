from django.urls import path
from . import views


urlpatterns = [
    path('reviews/', views.review_read_create),
    path('reviews/<int:review_pk>', views.review_detail_update_delete),
    path('reviews/<int:review_pk>/comment/', views.create_comment),
    path('reviews/<int:review_pk>/comment/<int:comment_pk>/', views.comment_update_delete),
]
