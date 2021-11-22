from django.contrib import admin
from .models import MovieReview, ActorReview, MovieComment, ActorComment


admin.site.register(MovieReview)
admin.site.register(ActorReview)
admin.site.register(MovieComment)
admin.site.register(ActorComment)
