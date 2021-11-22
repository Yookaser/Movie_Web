import random

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from movies.models import Movie
from .models import MovieRating
from movies.models import Movie
from .serializers import RatingSerializer 
from movies.serializers import MovieSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_rating_read(request, movie_pk):
    reviews = MovieRating.objects.filter(movie=movie_pk)
    serializer = RatingSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def movie_rating_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def movie_rating_update(request, rating_pk):
    rating = get_object_or_404(MovieRating, pk=rating_pk)
    serializer = RatingSerializer(instance=rating, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_rating_check(request, movie_pk, user_pk):
    review = MovieRating.objects.filter(movie=movie_pk).filter(user=user_pk)
    serializer = RatingSerializer(review, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def movie_recommend(request, user_pk):
    reviews = MovieRating.objects.filter(user=user_pk).order_by('-rank')

    if len(reviews) > 5:
        reviews = reviews[:5]

        watched = set()
        genres = {}
        for review in reviews:
            watched.add(review.movie.pk)
            for genre in Movie.objects.values('genres').filter(pk=review.movie.pk):
                key = genre['genres'] 
                if key in genres:
                    genres[key] += 1
                else:
                    genres[key] = 1

        recommend = []
        movies = Movie.objects.prefetch_related('genres').values().order_by('-vote_average')
        for movie in movies:
            if movie['vote_count'] < 100 or movie['id'] in watched: continue
            
            select = Movie.objects.values('genres').filter(pk=movie['id'])
 
            cnt = 0
            for genre in select:
                if genre['genres'] in genres:
                    cnt += 1
            
            if cnt and cnt >= len(select) // 2:    
                if (random.randrange(0, 4) < 3): continue

                recommend.append(movie)
                if len(recommend) == 7:
                    break

        serializer = MovieSerializer(recommend, many=True)
        return Response(serializer.data)
